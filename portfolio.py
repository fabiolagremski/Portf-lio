"""
Gerador de portfólio estático — Fabiola Gremski Mika
Execute: python gerar_portfolio.py
Resultado: index.html (pronto para GitHub Pages)
"""

# ── DADOS ────────────────────────────────────────────────────────────────────

PROFILE = {
    "name": "Fabiola Gremski Mika",
    "subtitle": (
        "Mestranda em Administração e Analista de Dados em formação. "
        "Desenvolvo dashboards em Power BI, análises com Python e SQL, "
        "transformando dados em informações para apoiar a tomada de decisão."
    ),
    # Coloque o caminho da sua foto aqui (ex: "assets/fabiola.jpg")
    # ou uma URL pública. Deixe vazio para exibir as iniciais.
    "photo": "",
}

ABOUT = {
    "highlight": "5+",
    "highlight_suffix": (
        "anos de experiência profissional em operações digitais, e-commerce, "
        "análise de indicadores e gestão de processos. Atualmente, sou mestranda "
        "em Administração pela PUCPR e estou em transição para a área de Dados, "
        "desenvolvendo projetos em Power BI, Python e SQL voltados à análise de "
        "negócios e apoio à tomada de decisão."
    ),
    "closing": (
        "Minha experiência combina visão estratégica, capacidade analítica e "
        "pesquisa acadêmica, permitindo transformar dados em insights relevantes "
        "para empresas e organizações."
    ),
}

SKILLS = [
    {
        "icon": "chart-bar",
        "title": "Visualização e Análise de Dados",
        "text": "Transformação de dados em informações estratégicas por meio de dashboards, indicadores e análises que apoiam a tomada de decisão.",
    },
    {
        "icon": "layout-dashboard",
        "title": "Business Intelligence",
        "text": "Desenvolvimento de dashboards interativos no Power BI, construção de KPIs e monitoramento de desempenho para diferentes áreas de negócio.",
    },
    {
        "icon": "code",
        "title": "Python e SQL",
        "text": "Manipulação, limpeza e análise de dados utilizando Python, SQL e bibliotecas voltadas para análise exploratória e automação de processos.",
    },
    {
        "icon": "microscope",
        "title": "Pesquisa e Analytics",
        "text": "Aplicação de métodos quantitativos, análise de comportamento do consumidor e desenvolvimento de pesquisas acadêmicas baseadas em evidências.",
    },
]

PROJECTS = [
    {
        "title": "Performance de Vendas & Devoluções Amazon",
        "objective": (
            "Desenvolver um dashboard interativo para análise do desempenho de vendas, "
            "comportamento de devoluções e indicadores comerciais em uma operação fictícia "
            "de e-commerce inspirada no ambiente Amazon."
        ),
        "indicators": [
            "Receita Bruta",
            "Total de Pedidos",
            "Total de Devoluções",
            "Total de Cancelamentos",
            "Avaliação Média dos Clientes",
            "Ticket Médio",
        ],
        "analyses": [
            "Evolução da receita ao longo dos anos",
            "Receita por categoria de produto",
            "Receita por faixa etária dos consumidores",
            "Receita por país",
            "Produtos com maior faturamento",
            "Categorias com maior índice de devolução",
        ],
        "technologies": "Power BI • Power Query • DAX",
        # Coloque o caminho da imagem (ex: "assets/dashboard.png") ou URL pública
        "image": "",
        "link": "#",
    },
    {
        "title": "Projeto Futuro",
        "objective": "Descrição do projeto.",
        "indicators": ["KPI 1", "KPI 2", "KPI 3"],
        "analyses": [],
        "technologies": "Power BI • SQL • Python",
        "image": "",
        "link": "#",
    },
    {
        "title": "Projeto Futuro",
        "objective": "Descrição do projeto.",
        "indicators": ["KPI 1", "KPI 2", "KPI 3"],
        "analyses": [],
        "technologies": "Power BI • SQL • Python",
        "image": "",
        "link": "#",
    },
]

HELP_ITEMS = [
    {
        "icon": "pie-chart",
        "title": "Business Intelligence",
        "text": "Transformação de dados em dashboards intuitivos e indicadores que facilitam o acompanhamento dos resultados.",
    },
    {
        "icon": "search",
        "title": "Análise de Negócios",
        "text": "Investigação de dados para identificar oportunidades, tendências e pontos de melhoria nos processos.",
    },
    {
        "icon": "lightbulb",
        "title": "Soluções Baseadas em Dados",
        "text": "Aplicação de Power BI, Python e SQL para apoiar decisões mais rápidas, eficientes e orientadas por evidências.",
    },
]

CONTACTS = [
    {
        "icon": "globe",
        "label": "Site",
        "value": "www.fabiolagmika.com.br",
        "href": "https://www.fabiolagmika.com.br",
    },
    {
        "icon": "mail",
        "label": "Email",
        "value": "fabigremski@gmail.com",
        "href": "mailto:fabigremski@gmail.com",
    },
    {
        "icon": "linkedin",
        "label": "LinkedIn",
        "value": "in/fabiola-gremski-mika",
        "href": "https://www.linkedin.com/in/fabiola-gremski-mika/",
    },
]

# ── ÍCONES SVG inline ─────────────────────────────────────────────────────────

ICONS = {
    "chart-bar": '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" viewBox="0 0 24 24"><line x1="18" y1="20" x2="18" y2="10"/><line x1="12" y1="20" x2="12" y2="4"/><line x1="6" y1="20" x2="6" y2="14"/><line x1="2" y1="20" x2="22" y2="20"/></svg>',
    "layout-dashboard": '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" viewBox="0 0 24 24"><rect x="3" y="3" width="7" height="9"/><rect x="14" y="3" width="7" height="5"/><rect x="14" y="12" width="7" height="9"/><rect x="3" y="16" width="7" height="5"/></svg>',
    "code": '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" viewBox="0 0 24 24"><polyline points="16 18 22 12 16 6"/><polyline points="8 6 2 12 8 18"/></svg>',
    "microscope": '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" viewBox="0 0 24 24"><path d="M6 18h8"/><path d="M3 22h18"/><path d="M14 22a7 7 0 1 0 0-14h-1"/><path d="M9 14h2"/><path d="M9 12a2 2 0 0 1-2-2V6h6v4a2 2 0 0 1-2 2Z"/><path d="M12 6V3a1 1 0 0 0-1-1H9a1 1 0 0 0-1 1v3"/></svg>',
    "pie-chart": '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" viewBox="0 0 24 24"><path d="M21.21 15.89A10 10 0 1 1 8 2.83"/><path d="M22 12A10 10 0 0 0 12 2v10z"/></svg>',
    "search": '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" viewBox="0 0 24 24"><circle cx="11" cy="11" r="8"/><line x1="21" y1="21" x2="16.65" y2="16.65"/></svg>',
    "lightbulb": '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" viewBox="0 0 24 24"><path d="M15 14c.2-1 .7-1.7 1.5-2.5 1-.9 1.5-2.2 1.5-3.5A6 6 0 0 0 6 8c0 1 .2 2.2 1.5 3.5.7.7 1.3 1.5 1.5 2.5"/><path d="M9 18h6"/><path d="M10 22h4"/></svg>',
    "globe": '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" viewBox="0 0 24 24"><circle cx="12" cy="12" r="10"/><line x1="2" y1="12" x2="22" y2="12"/><path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"/></svg>',
    "mail": '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" viewBox="0 0 24 24"><rect x="2" y="4" width="20" height="16" rx="2"/><path d="m22 7-8.97 5.7a1.94 1.94 0 0 1-2.06 0L2 7"/></svg>',
    "linkedin": '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" viewBox="0 0 24 24"><path d="M16 8a6 6 0 0 1 6 6v7h-4v-7a2 2 0 0 0-2-2 2 2 0 0 0-2 2v7h-4v-7a6 6 0 0 1 6-6z"/><rect x="2" y="9" width="4" height="12"/><circle cx="4" cy="4" r="2"/></svg>',
    "image": '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" viewBox="0 0 24 24"><rect x="3" y="3" width="18" height="18" rx="2"/><circle cx="9" cy="9" r="2"/><path d="m21 15-3.086-3.086a2 2 0 0 0-2.828 0L6 21"/></svg>',
    "arrow-right": '<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" viewBox="0 0 24 24"><line x1="5" y1="12" x2="19" y2="12"/><polyline points="12 5 19 12 12 19"/></svg>',
    "arrow-down": '<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" viewBox="0 0 24 24"><line x1="12" y1="5" x2="12" y2="19"/><polyline points="19 12 12 19 5 12"/></svg>',
}

# ── HELPERS ───────────────────────────────────────────────────────────────────

def icon(name: str) -> str:
    return ICONS.get(name, "")


def section_title(text: str) -> str:
    return f'<h2 class="section-title"><span class="lime">| </span>{text}</h2>'


def icon_box(name: str, extra_class: str = "") -> str:
    return f'<div class="icon-box {extra_class}">{icon(name)}</div>'


def render_photo() -> str:
    src = PROFILE.get("photo", "")
    name = PROFILE["name"]
    if src:
        return f'<img src="{src}" alt="Foto de {name}" class="profile-photo" />'
    initials = "".join(w[0] for w in name.split()[:2]).upper()
    return f'<div class="profile-photo profile-initials">{initials}</div>'


def render_skills() -> str:
    cards = ""
    for s in SKILLS:
        cards += f"""
        <article class="card skill-card">
          {icon_box(s["icon"])}
          <h3>{s["title"]}</h3>
          <p class="muted">{s["text"]}</p>
        </article>"""
    return f"""
    <section class="section">
      {section_title("Principais Habilidades")}
      <div class="grid grid-4">{cards}
      </div>
    </section>"""


def render_projects() -> str:
    cards = ""
    for p in PROJECTS:
        if p.get("image"):
            img_block = f'<img src="{p["image"]}" alt="{p["title"]}" loading="lazy" class="project-img" />'
        else:
            img_block = f'<div class="project-img-placeholder">{icon("image")}<span>Imagem em breve</span></div>'

        indicators_html = "".join(f"<li>• {ind}</li>" for ind in p["indicators"])
        analyses_html = ""
        if p.get("analyses"):
            items = "".join(f"<li>• {a}</li>" for a in p["analyses"])
            analyses_html = f'<p class="label-lime">Principais análises</p><ul class="list">{items}</ul>'

        link_attr = 'target="_blank" rel="noopener noreferrer"' if p["link"] != "#" else ""
        cards += f"""
        <article class="card project-card">
          <div class="project-thumb">{img_block}</div>
          <div class="project-body">
            <h3 class="project-title">{p["title"]}</h3>
            <p class="label-lime">Objetivo</p>
            <p class="muted small">{p["objective"]}</p>
            <p class="label-lime">Principais indicadores</p>
            <ul class="list">{indicators_html}</ul>
            {analyses_html}
            <p class="label-lime">Tecnologias utilizadas</p>
            <p class="muted small">{p["technologies"]}</p>
            <a href="{p["link"]}" {link_attr} class="btn btn-outline">
              Ver detalhes {icon("arrow-right")}
            </a>
          </div>
        </article>"""
    return f"""
    <section class="section">
      {section_title("Projetos Desenvolvidos")}
      <p class="muted section-desc">
        Explore alguns projetos que já desenvolvi. Nesta seção você encontrará
        projetos desenvolvidos durante minha transição para a área de Dados,
        envolvendo análise exploratória, construção de dashboards e visualização
        de indicadores de negócio utilizando Power BI, Python e SQL.
      </p>
      <div class="grid grid-3">{cards}
      </div>
    </section>"""


def render_help() -> str:
    cards = ""
    for h in HELP_ITEMS:
        cards += f"""
        <article class="card">
          {icon_box(h["icon"], "lime-bg")}
          <h3>{h["title"]}</h3>
          <p class="muted">{h["text"]}</p>
        </article>"""
    return f"""
    <section class="section">
      {section_title("Como posso te ajudar")}
      <p class="muted section-desc">Como posso ajudar empresas</p>
      <div class="grid grid-3">{cards}
      </div>
    </section>"""


def render_contacts() -> str:
    items = ""
    for c in CONTACTS:
        items += f"""
        <a href="{c["href"]}" target="_blank" rel="noopener noreferrer" class="contact-card">
          <span class="icon-box">{icon(c["icon"])}</span>
          <span>
            <span class="contact-label">{c["label"]}</span>
            <span class="contact-value muted">{c["value"]}</span>
          </span>
        </a>"""
    return f"""
    <section class="section">
      {section_title("Entre em contato comigo:")}
      <div class="contact-grid">{items}
      </div>
    </section>"""


# ── TEMPLATE HTML ─────────────────────────────────────────────────────────────

CSS = """
  @import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;500;600;700&display=swap');

  *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }

  :root {
    --bg:        #1a1a2e;
    --bg-card:   #21213a;
    --fg:        #f7f7fb;
    --muted:     #9898b8;
    --border:    #2e2e4a;
    --lime:      #cdff4e;
    --purple:    #6558fe;
    --radius:    14px;
  }

  html { scroll-behavior: smooth; }

  body {
    background: var(--bg);
    color: var(--fg);
    font-family: 'Space Grotesk', sans-serif;
    -webkit-font-smoothing: antialiased;
    line-height: 1.6;
  }

  /* ── HERO ── */
  .hero {
    background:
      radial-gradient(120% 120% at 80% 0%, rgba(101,88,254,.45) 0%, transparent 55%),
      radial-gradient(100% 100% at 0% 100%, rgba(60,40,200,.35) 0%, transparent 50%);
    padding: 5rem 1.5rem;
  }
  .hero-inner {
    max-width: 72rem;
    margin: 0 auto;
    display: grid;
    grid-template-columns: 1fr auto;
    gap: 2.5rem;
    align-items: center;
  }
  @media (max-width: 640px) {
    .hero-inner { grid-template-columns: 1fr; }
    .hero-photo { order: -1; display: flex; justify-content: center; }
  }
  .hero-eyebrow {
    font-size: .75rem;
    font-weight: 600;
    letter-spacing: .2em;
    text-transform: uppercase;
    color: var(--lime);
    margin-bottom: 1rem;
  }
  .hero h1 { font-size: clamp(2rem, 6vw, 3.5rem); font-weight: 700; line-height: 1.15; }
  .hero-sub { margin-top: 1.25rem; color: var(--muted); font-size: 1.05rem; max-width: 36rem; }

  /* ── FOTO ── */
  .profile-photo {
    width: 200px; height: 200px;
    border-radius: 50%;
    border: 4px solid rgba(205,255,78,.7);
    object-fit: cover;
    box-shadow: 0 0 60px -10px rgba(101,88,254,.5);
  }
  .profile-initials {
    display: flex; align-items: center; justify-content: center;
    background: rgba(101,88,254,.2);
    font-size: 2.5rem; font-weight: 700; color: var(--lime);
  }

  /* ── BTN ── */
  .btn {
    display: inline-flex; align-items: center; gap: .5rem;
    padding: .75rem 1.5rem; border-radius: var(--radius);
    font-weight: 600; font-size: .95rem; text-decoration: none;
    transition: opacity .2s;
    margin-top: 2rem;
  }
  .btn:hover { opacity: .85; }
  .btn-lime { background: var(--lime); color: #111; }
  .btn-outline { border: 1px solid var(--border); color: var(--fg); width: 100%; justify-content: center; margin-top: 1.25rem; }
  .btn-outline:hover { border-color: var(--lime); }

  /* ── SECTIONS ── */
  .section { max-width: 72rem; margin: 0 auto; padding: 5rem 1.5rem; }
  .section-title { font-size: clamp(1.6rem, 4vw, 2.25rem); font-weight: 700; margin-bottom: 2rem; }
  .section-desc { color: var(--muted); margin-bottom: 2.5rem; max-width: 48rem; margin-top: -.5rem; }
  .lime { color: var(--lime); }
  .muted { color: var(--muted); }
  .small { font-size: .875rem; }

  /* ── GRID ── */
  .grid { display: grid; gap: 1.5rem; }
  .grid-4 { grid-template-columns: repeat(auto-fill, minmax(220px, 1fr)); }
  .grid-3 { grid-template-columns: repeat(auto-fill, minmax(280px, 1fr)); }

  /* ── CARDS ── */
  .card {
    background: var(--bg-card);
    border: 1px solid var(--border);
    border-radius: var(--radius);
    padding: 1.5rem;
    box-shadow: 0 18px 50px -20px rgba(10,10,20,.8);
    transition: border-color .2s;
  }
  .card:hover { border-color: var(--purple); }
  .card h3 { font-size: 1rem; font-weight: 600; margin-bottom: .75rem; }
  .card p { font-size: .875rem; line-height: 1.65; }

  /* ── ICON BOX ── */
  .icon-box {
    display: inline-flex; align-items: center; justify-content: center;
    width: 3rem; height: 3rem;
    border-radius: 12px;
    background: rgba(101,88,254,.15);
    color: var(--lime);
    margin-bottom: 1.25rem;
  }
  .icon-box.lime-bg { background: rgba(205,255,78,.12); }

  /* ── SOBRE MIM ── */
  .about-section { max-width: 52rem; margin: 0 auto; padding: 5rem 1.5rem; }
  .about-highlight { font-size: clamp(2.5rem, 6vw, 3.5rem); font-weight: 700; color: var(--lime); margin-right: .5rem; }
  .about-text { color: var(--muted); font-size: 1.05rem; margin-top: 1.25rem; line-height: 1.8; }

  /* ── PROJECTS ── */
  .project-card { padding: 0; overflow: hidden; display: flex; flex-direction: column; }
  .project-thumb { aspect-ratio: 16/10; width: 100%; overflow: hidden; background: var(--border); }
  .project-img { width: 100%; height: 100%; object-fit: cover; }
  .project-img-placeholder {
    width: 100%; height: 100%;
    display: flex; flex-direction: column; align-items: center; justify-content: center;
    gap: .5rem; color: var(--muted); font-size: .75rem;
  }
  .project-body { padding: 1.5rem; flex: 1; display: flex; flex-direction: column; }
  .project-title { font-size: .875rem; font-weight: 700; text-transform: uppercase; letter-spacing: .05em; margin-bottom: .75rem; }
  .label-lime { font-size: .875rem; font-weight: 600; color: var(--lime); margin-top: 1rem; margin-bottom: .25rem; }
  .list { list-style: none; font-size: .875rem; color: var(--muted); display: flex; flex-direction: column; gap: .2rem; }

  /* ── CONTACTS ── */
  .contact-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(220px, 1fr)); gap: 1.5rem; margin-top: 2rem; }
  .contact-card {
    display: flex; align-items: center; gap: 1rem;
    background: var(--bg-card); border: 1px solid var(--border);
    border-radius: var(--radius); padding: 1.5rem;
    text-decoration: none; color: inherit;
    box-shadow: 0 18px 50px -20px rgba(10,10,20,.8);
    transition: border-color .2s;
  }
  .contact-card:hover { border-color: var(--lime); }
  .contact-label { display: block; font-size: .875rem; font-weight: 600; }
  .contact-value { display: block; font-size: .8rem; word-break: break-all; }

  /* ── FOOTER ── */
  footer {
    border-top: 1px solid var(--border);
    text-align: center; padding: 2rem 1.5rem;
    font-size: .875rem; color: var(--muted);
  }
"""


def build_html() -> str:
    from datetime import date

    name = PROFILE["name"]
    year = date.today().year

    hero = f"""
    <section class="hero">
      <div class="hero-inner">
        <div>
          <p class="hero-eyebrow">Analista de Dados</p>
          <h1><span class="lime">Fabiola</span> Gremski Mika</h1>
          <p class="hero-sub">{PROFILE["subtitle"]}</p>
          <a href="#sobre-mim" class="btn btn-lime">
            Sobre mim {icon("arrow-down")}
          </a>
        </div>
        <div class="hero-photo">
          <div style="position:relative">
            {render_photo()}
          </div>
        </div>
      </div>
    </section>"""

    about_section = f"""
    <section id="sobre-mim" class="about-section">
      {section_title("Sobre mim")}
      <p style="color:var(--fg)">Seja muito bem-vindo(a) ao meu portfólio. Conheça a minha trajetória.</p>
      <p class="about-text">
        <span class="about-highlight">{ABOUT["highlight"]}</span>
        {ABOUT["highlight_suffix"]}
      </p>
      <p class="about-text">{ABOUT["closing"]}</p>
    </section>"""

    return f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>{name} — Analista de Dados</title>
  <meta name="description" content="Portfólio de {name}, Analista de Dados em formação. Dashboards em Power BI, análises com Python e SQL para apoiar a tomada de decisão." />
  <meta property="og:title" content="{name} — Analista de Dados" />
  <meta property="og:description" content="Dashboards em Power BI, análises com Python e SQL — transformando dados em decisões." />
  <meta property="og:type" content="website" />
  <style>{CSS}</style>
</head>
<body>
  {hero}
  {about_section}
  {render_skills()}
  {render_projects()}
  {render_help()}
  {render_contacts()}
  <footer>© {year} {name}</footer>
</body>
</html>"""


# ── MAIN ──────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    html = build_html()
    output = "index.html"
    with open(output, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"✅  Portfólio gerado: {output}")
    print("👉  Para subir no GitHub Pages:")
    print("    1. Coloque index.html na raiz do repositório")
    print("    2. Ative GitHub Pages em Settings → Pages → Branch: main")
    print("    3. Aponte seu domínio nas configurações de DNS")
