-- Postgres do app. Isolamento de tenant é reforçado por ROW-LEVEL SECURITY,
-- não só por filtro na aplicação (filtro em app é burlável por bug).
-- PII do cliente é criptografada em repouso; o estado do Flow (na AMP) é pseudonimizado.

create extension if not exists pgcrypto;

create table tenants (
  id uuid primary key default gen_random_uuid(),
  nome text not null,
  criado_em timestamptz not null default now()
);

create table profissionais (
  id uuid primary key default gen_random_uuid(),
  tenant_id uuid not null references tenants(id),
  nome text not null,
  oab text,
  email text not null unique,
  criado_em timestamptz not null default now()
);

create table casos (
  id uuid primary key default gen_random_uuid(),
  tenant_id uuid not null references tenants(id),
  profissional_id uuid not null references profissionais(id),
  cliente_nome_cifrado bytea not null,        -- PII cifrada (pgp_sym_encrypt); nunca em claro
  status text not null default 'intake',
  task_id text,                               -- execução na CrewAI AMP
  versao_corpus text,
  teto_usd_caso numeric not null default 5.0,
  custo_usd numeric not null default 0.0,
  criado_em timestamptz not null default now(),
  expira_em timestamptz not null             -- TTL LGPD: job apaga estado do Flow + este registro
);

create table fila_revisao (
  id uuid primary key default gen_random_uuid(),
  caso_id uuid not null references casos(id),
  tenant_id uuid not null references tenants(id),
  execution_id text not null,
  task_id text not null,
  payload jsonb not null,                     -- vindo do webhook HITL da AMP
  decisao text,                               -- aprovado | rejeitado | revisar
  feedback text,
  decidido_por uuid references profissionais(id),
  decidido_em timestamptz
);

-- RLS: cada linha só é visível/mutável dentro do seu tenant.
-- O app seta `set local app.tenant_id = '<uuid>'` por request (do token/sessão).
alter table casos enable row level security;
alter table fila_revisao enable row level security;
alter table profissionais enable row level security;

create policy caso_tenant_isolation on casos
  using (tenant_id = current_setting('app.tenant_id')::uuid);
create policy fila_tenant_isolation on fila_revisao
  using (tenant_id = current_setting('app.tenant_id')::uuid);
create policy prof_tenant_isolation on profissionais
  using (tenant_id = current_setting('app.tenant_id')::uuid);

-- Índice para o job de deleção LGPD (right-to-erasure por vencimento).
create index casos_expira_em_idx on casos (expira_em);
