"""
portfolio.py — Portfólio de Fabiola Gremski Mika
==================================================
Execute:
    pip install flask
    python portfolio.py

Acesse: http://localhost:5000
"""

from flask import Flask, render_template_string, request, jsonify

app = Flask(__name__)

# ─────────────────────────────────────────────
#  DADOS DO PORTFÓLIO
# ─────────────────────────────────────────────

DADOS = {
    "nome": "Fabiola Gremski Mika",
    "titulo": "Analista de Dados Jr",
    "subtitulo": "Power BI · SQL · Python · Business Analytics",
    "localizacao": "Curitiba – PR",
    "sobre": [
        "Sou Fabiola, analista de dados em formação sólida, tanto na teoria quanto na prática. "
        "Minha trajetória mistura gestão de e-commerce, coordenação de relacionamento com clientes "
        "e pesquisa científica financiada pela CAPES, o que me deu algo raro: a capacidade de ler "
        "dados sem perder o contexto humano e de negócio por trás deles.",

        "Atualmente sou mestranda em Administração pela PUCPR, desenvolvendo pesquisa experimental "
        "quantitativa com delineamento fatorial, e simultaneamente cursando MBA em Ciência de Dados "
        "e Inteligência Artificial pela Uninter. É muita coisa em paralelo. Mas eu funciono bem assim.",

        "Meu interesse está na intersecção entre análise rigorosa e comunicação clara: "
        "não basta encontrar o padrão, é preciso saber contá-lo para quem vai tomar a decisão.",
    ],
    "stats": [
        {"valor": "~580", "label": "participantes por estudo na pesquisa de mestrado"},
        {"valor": "2×2",  "label": "delineamento fatorial experimental"},
        {"valor": "3+",   "label": "anos combinando dados e gestão de negócios"},
        {"valor": "2027", "label": "previsão de conclusão do mestrado"},
    ],
    "competencias": [
        {
            "icone": "🐍",
            "nome": "Python & Dados",
            "tags": ["Python", "Pandas", "NumPy", "Matplotlib", "SciPy", "Statsmodels", "Scikit-Learn"],
        },
        {
            "icone": "🗄️",
            "nome": "SQL & Banco de Dados",
            "tags": ["SQL", "Consultas complexas", "ETL", "Qualidade de Dados"],
        },
        {
            "icone": "📊",
            "nome": "Business Intelligence",
            "tags": ["Power BI", "DAX", "Excel", "KPIs", "Dashboards", "Storytelling"],
        },
        {
            "icone": "📐",
            "nome": "Estatística & Pesquisa",
            "tags": ["EDA", "Estatística Descritiva", "Testes de Hipótese",
                     "Pesquisa Quantitativa", "Escalas Psicométricas"],
        },
        {
            "icone": "🤖",
            "nome": "Machine Learning",
            "tags": ["Scikit-Learn", "Classificação", "Aprendizado Supervisionado", "Modelagem Preditiva"],
        },
        {
            "icone": "🔧",
            "nome": "Ferramentas & Plataformas",
            "tags": ["Power Automate", "SAP", "GitHub", "Jupyter Notebook",
                     "Google Colab", "Pacote Office"],
        },
    ],
    "experiencias": [
        {
            "cargo": "Pesquisadora Científica",
            "empresa": "CAPES / PUCPR",
            "atividades": [
                "Desenvolvimento de pesquisas quantitativas e experimentais com rigor metodológico",
                "Construção de instrumentos de coleta e escalas psicométricas validadas",
                "Análise de comportamento do consumidor com pipeline estatístico completo",
                "Produção de relatórios analíticos e comunicação de resultados",
            ],
            "chips": ["Estatística Aplicada", "Pesquisa Quantitativa", "Python", "Inferência Estatística"],
        },
        {
            "cargo": "Gestora de E-commerce",
            "empresa": "FGM Empreendimentos Digitais",
            "atividades": [
                "Monitoramento de indicadores de desempenho e KPIs da operação",
                "Gestão de dados operacionais e relatórios gerenciais",
                "Análise de experiência do cliente orientada por dados",
            ],
            "chips": ["Business Analytics", "Excel", "CRM", "Tomada de Decisão"],
        },
        {
            "cargo": "Coordenadora de CRC",
            "empresa": "Metta Distribuidora",
            "atividades": [
                "Consolidação de indicadores comerciais e gestão de CRM",
                "Produção de relatórios executivos e organização de processos",
                "Eficiência operacional baseada em análise de dados",
            ],
            "chips": ["CRM Analytics", "Relatórios Executivos", "Gestão de Dados"],
        },
    ],
    "projetos": [
        {
            "tipo": "Business Intelligence",
            "nome": "Dashboard de Vendas",
            "desc": "Análise de indicadores comerciais com acompanhamento de faturamento, "
                    "ticket médio, volume de vendas e comportamento dos clientes — "
                    "storytelling visual orientado à decisão gerencial.",
            "tags": ["Power BI", "Excel", "DAX"],
        },
        {
            "tipo": "Business Intelligence",
            "nome": "Dashboard de Clientes",
            "desc": "Projeto voltado à análise de perfil de clientes, comportamento de "
                    "compra e indicadores de relacionamento com foco em segmentação e CRM Analytics.",
            "tags": ["Power BI", "Excel", "Segmentação"],
        },
        {
            "tipo": "Python · EDA",
            "nome": "Análise Exploratória de Dados",
            "desc": "Exploração e limpeza de bases de dados para identificação de padrões, "
                    "inconsistências e oportunidades de negócio — com visualizações analíticas "
                    "e data wrangling avançado.",
            "tags": ["Python", "Pandas", "NumPy", "Matplotlib"],
        },
        {
            "tipo": "Python · ETL",
            "nome": "ETL e Transformação de Dados",
            "desc": "Tratamento, transformação e preparação de dados para análise — "
                    "com foco em qualidade dos dados, padronização e construção "
                    "de pipelines reproduzíveis.",
            "tags": ["Python", "Pandas", "ETL"],
        },
        {
            "tipo": "Machine Learning",
            "nome": "Estudos de Classificação",
            "desc": "Projetos de aprendizado supervisionado para classificação de dados "
                    "com Scikit-Learn — modelagem preditiva com foco em interpretabilidade "
                    "e avaliação de desempenho.",
            "tags": ["Python", "Scikit-Learn", "ML"],
        },
    ],
    "pesquisa": {
        "titulo": "Corpos como objetos ou conflitos morais? Mecanismos psicológicos da sexualização masculina na publicidade",
        "pergunta": "Como diferentes níveis de sexualização masculina e tipos de apelo publicitário "
                    "influenciam a percepção dos consumidores e a avaliação das marcas?",
        "descricao": "Pesquisa experimental que investiga como diferentes níveis de sexualização masculina "
                     "em anúncios influenciam atitudes em relação à marca, intenção de compra e julgamentos "
                     "morais dos consumidores. O projeto utiliza métodos quantitativos para compreender os "
                     "mecanismos psicológicos que explicam as respostas dos consumidores diante de diferentes "
                     "estratégias publicitárias.",
        "metodologia": [
            "Delineamento fatorial 2×2",
            "Dois estudos independentes",
            "~580 participantes por estudo",
            "Coleta online",
            "Escalas psicométricas validadas",
        ],
        "pipeline": [
            "Limpeza e EDA",
            "Estatística descritiva",
            "Testes de hipóteses",
            "Modelagem estatística",
            "Visualização dos resultados",
        ],
        "ferramentas": ["Python", "SciPy", "Statsmodels", "Scikit-Learn", "Jupyter"],
        "status": "Em desenvolvimento · Conclusão prevista 2027",
    },
    "contatos": {
        "linkedin": "https://linkedin.com/in/",   # ← substitua pelo seu
        "github":   "https://github.com/",         # ← substitua pelo seu
        "email":    "mailto:seuemail@email.com",   # ← substitua pelo seu
        "whatsapp": "https://wa.me/5541999999999", # ← substitua pelo seu
    },
}

# ─────────────────────────────────────────────
#  TEMPLATE HTML
# ─────────────────────────────────────────────

HTML = """<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="UTF-8"/>
  <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
  <title>{{ d.nome }} — Analista de Dados</title>
  <link rel="preconnect" href="https://fonts.googleapis.com"/>
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin/>
  <link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@300;400;500;600;700&family=Inter:wght@300;400;500&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet"/>
  <style>
    *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }
    :root {
      --bg-deep:      #080D1A;
      --bg-surface:   #0F172A;
      --bg-card:      #131D35;
      --blue-royal:   #2563EB;
      --blue-light:   #60A5FA;
      --blue-glow:    #3B82F6;
      --blue-subtle:  #1E3A6E;
      --text-primary: #E2E8F0;
      --text-secondary:#94A3B8;
      --text-muted:   #4B617A;
      --border:       #1E3A6E;
      --border-light: #2563EB33;
      --mono: 'JetBrains Mono', monospace;
      --sans: 'Space Grotesk', sans-serif;
      --body: 'Inter', sans-serif;
    }
    html { scroll-behavior: smooth; }
    body { background: var(--bg-deep); color: var(--text-primary); font-family: var(--body); font-size:16px; line-height:1.6; overflow-x:hidden; }

    /* NAV */
    nav { position:fixed; top:0; left:0; right:0; z-index:100; display:flex; align-items:center; justify-content:space-between; padding:1rem 3rem; background:rgba(8,13,26,.88); backdrop-filter:blur(16px); border-bottom:1px solid var(--border); }
    .nav-logo { font-family:var(--mono); font-size:.85rem; color:var(--blue-light); letter-spacing:.05em; }
    .nav-links { display:flex; gap:2rem; list-style:none; }
    .nav-links a { font-family:var(--sans); font-size:.85rem; font-weight:500; color:var(--text-secondary); text-decoration:none; letter-spacing:.04em; transition:color .2s; }
    .nav-links a:hover { color:var(--blue-light); }

    /* HERO */
    #home { min-height:100vh; display:flex; align-items:center; padding:7rem 3rem 4rem; position:relative; overflow:hidden; }
    .hero-grid-bg { position:absolute; inset:0; z-index:0; background-image: linear-gradient(var(--border) 1px, transparent 1px), linear-gradient(90deg, var(--border) 1px, transparent 1px); background-size:60px 60px; opacity:.18; mask-image:radial-gradient(ellipse 80% 60% at 50% 50%, black 40%, transparent 100%); }
    .hero-glow { position:absolute; width:600px; height:600px; border-radius:50%; background:radial-gradient(circle, rgba(37,99,235,.15) 0%, transparent 70%); top:10%; left:-10%; pointer-events:none; }
    .hero-content { position:relative; z-index:1; max-width:820px; }
    .hero-eyebrow { font-family:var(--mono); font-size:.8rem; color:var(--blue-light); letter-spacing:.1em; margin-bottom:1.5rem; display:flex; align-items:center; gap:.75rem; }
    .hero-eyebrow::before { content:''; display:block; width:2rem; height:1px; background:var(--blue-light); }
    .hero-name { font-family:var(--sans); font-size:clamp(2.4rem,5vw,4rem); font-weight:700; line-height:1.1; margin-bottom:.5rem; }
    .hero-title { font-family:var(--sans); font-size:clamp(1rem,2vw,1.3rem); font-weight:400; color:var(--blue-light); margin-bottom:1.75rem; }

    /* Terminal */
    .terminal { background:#0A0F1E; border:1px solid var(--border); border-radius:10px; padding:1.25rem 1.5rem; margin-bottom:2rem; max-width:520px; box-shadow:0 0 40px rgba(37,99,235,.12); }
    .terminal-header { display:flex; gap:6px; margin-bottom:1rem; }
    .terminal-dot { width:11px; height:11px; border-radius:50%; }
    .dot-r{background:#FF5F57;} .dot-y{background:#FFBD2E;} .dot-g{background:#28C840;}
    .terminal-line { font-family:var(--mono); font-size:.82rem; line-height:1.8; color:var(--text-secondary); }
    .t-prompt{color:#3B82F6;} .t-fn{color:#C084FC;} .t-str{color:#86EFAC;} .t-output{color:var(--text-primary);} .t-comment{color:var(--text-muted); font-style:italic;}
    .cursor { display:inline-block; width:8px; height:1em; background:var(--blue-light); vertical-align:text-bottom; animation:blink 1s step-end infinite; }
    @keyframes blink { 50%{opacity:0;} }

    .hero-desc { font-size:1rem; color:var(--text-secondary); max-width:560px; line-height:1.75; margin-bottom:2.5rem; }
    .hero-actions { display:flex; gap:1rem; flex-wrap:wrap; }
    .btn-primary { display:inline-flex; align-items:center; gap:.5rem; padding:.75rem 1.75rem; background:var(--blue-royal); color:#fff; font-family:var(--sans); font-size:.9rem; font-weight:600; border-radius:6px; text-decoration:none; border:none; cursor:pointer; transition:background .2s,transform .15s; }
    .btn-primary:hover { background:#1D4ED8; transform:translateY(-2px); }
    .btn-outline { display:inline-flex; align-items:center; gap:.5rem; padding:.75rem 1.75rem; border:1px solid var(--border); color:var(--text-secondary); font-family:var(--sans); font-size:.9rem; font-weight:500; border-radius:6px; text-decoration:none; transition:border-color .2s,color .2s,transform .15s; }
    .btn-outline:hover { border-color:var(--blue-light); color:var(--blue-light); transform:translateY(-2px); }

    /* SEÇÕES */
    section { padding:6rem 3rem; max-width:1100px; margin:0 auto; }
    .section-label { font-family:var(--mono); font-size:.75rem; color:var(--blue-light); letter-spacing:.12em; text-transform:uppercase; margin-bottom:.5rem; }
    .section-title { font-family:var(--sans); font-size:clamp(1.6rem,3vw,2.2rem); font-weight:700; margin-bottom:3rem; }
    .section-divider { width:100%; height:1px; background:linear-gradient(90deg, var(--blue-royal), transparent); margin-bottom:3rem; }

    /* SOBRE */
    .sobre-grid { display:grid; grid-template-columns:1fr 1fr; gap:4rem; align-items:start; }
    .sobre-text p { color:var(--text-secondary); margin-bottom:1rem; line-height:1.8; }
    .sobre-stats { display:grid; grid-template-columns:1fr 1fr; gap:1rem; }
    .stat-card { background:var(--bg-card); border:1px solid var(--border); border-radius:8px; padding:1.25rem; transition:border-color .2s; }
    .stat-card:hover { border-color:var(--blue-royal); }
    .stat-value { font-family:var(--sans); font-size:1.8rem; font-weight:700; color:var(--blue-light); line-height:1; margin-bottom:.3rem; }
    .stat-label { font-size:.8rem; color:var(--text-muted); }

    /* COMPETÊNCIAS */
    .skills-grid { display:grid; grid-template-columns:repeat(auto-fill,minmax(280px,1fr)); gap:1.25rem; }
    .skill-category { background:var(--bg-card); border:1px solid var(--border); border-radius:10px; padding:1.5rem; transition:border-color .25s,transform .2s; }
    .skill-category:hover { border-color:var(--blue-royal); transform:translateY(-3px); }
    .skill-cat-icon { font-size:1.4rem; margin-bottom:.75rem; }
    .skill-cat-name { font-family:var(--sans); font-size:.95rem; font-weight:600; margin-bottom:.75rem; }
    .skill-tags { display:flex; flex-wrap:wrap; gap:.4rem; }
    .tag { font-family:var(--mono); font-size:.72rem; padding:.25rem .6rem; background:var(--blue-subtle); color:var(--blue-light); border-radius:4px; border:1px solid var(--border-light); }

    /* EXPERIÊNCIA */
    .exp-timeline { position:relative; padding-left:2rem; }
    .exp-timeline::before { content:''; position:absolute; left:0; top:0; bottom:0; width:1px; background:linear-gradient(180deg, var(--blue-royal), transparent); }
    .exp-item { position:relative; margin-bottom:3rem; padding-left:1.5rem; }
    .exp-item::before { content:''; position:absolute; left:-2.375rem; top:.35rem; width:10px; height:10px; border-radius:50%; background:var(--blue-royal); box-shadow:0 0 10px var(--blue-glow); }
    .exp-role { font-family:var(--sans); font-size:1.05rem; font-weight:600; }
    .exp-company { font-family:var(--mono); font-size:.8rem; color:var(--blue-light); margin-bottom:.75rem; }
    .exp-list { list-style:none; display:flex; flex-direction:column; gap:.4rem; }
    .exp-list li { font-size:.9rem; color:var(--text-secondary); padding-left:1rem; position:relative; }
    .exp-list li::before { content:'›'; position:absolute; left:0; color:var(--blue-royal); font-weight:700; }
    .exp-chips { display:flex; flex-wrap:wrap; gap:.35rem; margin-top:.85rem; }
    .chip { font-size:.72rem; font-family:var(--mono); padding:.2rem .55rem; border-radius:3px; background:var(--bg-surface); border:1px solid var(--border); color:var(--text-muted); }

    /* PROJETOS */
    .projects-grid { display:grid; grid-template-columns:repeat(auto-fill,minmax(320px,1fr)); gap:1.25rem; }
    .project-card { background:var(--bg-card); border:1px solid var(--border); border-radius:10px; padding:1.75rem; display:flex; flex-direction:column; transition:border-color .25s,transform .2s,box-shadow .2s; }
    .project-card:hover { border-color:var(--blue-royal); transform:translateY(-4px); box-shadow:0 12px 40px rgba(37,99,235,.15); }
    .project-type { font-family:var(--mono); font-size:.7rem; color:var(--blue-light); letter-spacing:.1em; text-transform:uppercase; margin-bottom:.75rem; }
    .project-name { font-family:var(--sans); font-size:1.05rem; font-weight:600; margin-bottom:.6rem; }
    .project-desc { font-size:.875rem; color:var(--text-secondary); line-height:1.65; flex:1; margin-bottom:1.25rem; }

    /* PESQUISA */
    .research-card { background:var(--bg-card); border:1px solid var(--border); border-radius:12px; padding:2.5rem; display:grid; grid-template-columns:1fr 1fr; gap:3rem; }
    .research-title { font-family:var(--sans); font-size:1.2rem; font-weight:600; margin-bottom:.75rem; line-height:1.4; }
    .research-question { font-style:italic; font-size:.9rem; color:var(--blue-light); border-left:2px solid var(--blue-royal); padding-left:1rem; margin:1rem 0; line-height:1.6; }
    .research-desc { font-size:.875rem; color:var(--text-secondary); line-height:1.75; }
    .research-meta h4 { font-family:var(--sans); font-size:.8rem; font-weight:600; color:var(--text-muted); text-transform:uppercase; letter-spacing:.08em; margin-bottom:.5rem; margin-top:1.25rem; }
    .research-meta ul { list-style:none; }
    .research-meta li { font-size:.85rem; color:var(--text-secondary); padding:.2rem 0; }
    .status-badge { display:inline-flex; align-items:center; gap:.4rem; padding:.35rem .9rem; background:rgba(37,99,235,.1); border:1px solid var(--blue-royal); border-radius:20px; font-size:.75rem; font-family:var(--mono); color:var(--blue-light); margin-top:1.25rem; }
    .status-dot { width:6px; height:6px; border-radius:50%; background:var(--blue-light); animation:pulse 2s infinite; }
    @keyframes pulse { 0%,100%{opacity:1;} 50%{opacity:.3;} }

    /* CONTATO */
    #contato { text-align:center; }
    .contact-subtitle { font-size:1rem; color:var(--text-secondary); max-width:480px; margin:0 auto 3rem; line-height:1.75; }
    .contact-links { display:flex; justify-content:center; flex-wrap:wrap; gap:1rem; }
    .contact-btn { display:inline-flex; align-items:center; gap:.65rem; padding:.9rem 1.75rem; background:var(--bg-card); border:1px solid var(--border); border-radius:8px; color:var(--text-secondary); font-family:var(--sans); font-size:.9rem; font-weight:500; text-decoration:none; transition:border-color .2s,color .2s,transform .15s; }
    .contact-btn:hover { border-color:var(--blue-light); color:var(--blue-light); transform:translateY(-2px); }
    .contact-btn svg { width:18px; height:18px; fill:currentColor; }

    /* FORM */
    #fale-comigo { background:var(--bg-surface); padding:6rem 3rem; }
    #fale-comigo > div { max-width:600px; margin:0 auto; }
    .form-group { margin-bottom:1.25rem; }
    .form-title { font-family:var(--sans); font-size:clamp(1.6rem,3vw,2.2rem); font-weight:700; margin-bottom:.5rem; }
    label { display:block; font-family:var(--sans); font-size:.82rem; font-weight:500; color:var(--text-muted); text-transform:uppercase; letter-spacing:.06em; margin-bottom:.4rem; }
    input, textarea { width:100%; background:var(--bg-card); border:1px solid var(--border); border-radius:6px; color:var(--text-primary); font-family:var(--body); font-size:.9rem; padding:.8rem 1rem; outline:none; transition:border-color .2s; }
    input:focus, textarea:focus { border-color:var(--blue-royal); }
    textarea { resize:vertical; min-height:130px; }
    #msg-feedback { margin-top:1rem; font-family:var(--mono); font-size:.85rem; color:var(--blue-light); display:none; }

    /* FOOTER */
    footer { text-align:center; padding:2rem 3rem; border-top:1px solid var(--border); font-family:var(--mono); font-size:.75rem; color:var(--text-muted); }
    footer span { color:var(--blue-light); }

    /* REVEAL */
    .reveal { opacity:0; transform:translateY(24px); transition:opacity .55s ease,transform .55s ease; }
    .reveal.visible { opacity:1; transform:none; }

    @media(max-width:768px){
      nav{padding:1rem 1.5rem;}
      .nav-links{display:none;}
      section{padding:4rem 1.5rem;}
      #home{padding:6rem 1.5rem 3rem;}
      .sobre-grid,.research-card{grid-template-columns:1fr; gap:2rem;}
      #fale-comigo{padding:4rem 1.5rem;}
    }
  </style>
</head>
<body>

<nav>
  <div class="nav-logo">fgm.py</div>
  <ul class="nav-links">
    <li><a href="#home">Início</a></li>
    <li><a href="#sobre">Sobre</a></li>
    <li><a href="#competencias">Competências</a></li>
    <li><a href="#experiencia">Experiência</a></li>
    <li><a href="#projetos">Projetos</a></li>
    <li><a href="#pesquisa">Pesquisa</a></li>
    <li><a href="#fale-comigo">Contato</a></li>
  </ul>
</nav>

<!-- HERO -->
<div id="home">
  <div class="hero-grid-bg"></div>
  <div class="hero-glow"></div>
  <div class="hero-content">
    <div class="hero-eyebrow">{{ d.titulo }}</div>
    <h1 class="hero-name">{{ d.nome }}</h1>
    <p class="hero-title">{{ d.subtitulo }}</p>
    <div class="terminal">
      <div class="terminal-header">
        <div class="terminal-dot dot-r"></div>
        <div class="terminal-dot dot-y"></div>
        <div class="terminal-dot dot-g"></div>
      </div>
      <div class="terminal-line"><span class="t-comment"># Analista de Dados em construção contínua</span></div>
      <div class="terminal-line"><span class="t-prompt">&gt;&gt;&gt; </span><span class="t-fn">perfil</span> = {</div>
      <div class="terminal-line">&nbsp;&nbsp;&nbsp;&nbsp;<span class="t-str">"stack"</span>: [<span class="t-str">"Python"</span>, <span class="t-str">"SQL"</span>, <span class="t-str">"Power BI"</span>],</div>
      <div class="terminal-line">&nbsp;&nbsp;&nbsp;&nbsp;<span class="t-str">"formação"</span>: <span class="t-str">"Mestrado PUCPR + MBA IA"</span>,</div>
      <div class="terminal-line">&nbsp;&nbsp;&nbsp;&nbsp;<span class="t-str">"localização"</span>: <span class="t-str">"{{ d.localizacao }}"</span></div>
      <div class="terminal-line">}</div>
      <div class="terminal-line"><span class="t-prompt">&gt;&gt;&gt; </span><span class="t-fn">print</span>(<span class="t-str">"Dados → Decisões → Impacto"</span>)<span class="cursor"></span></div>
      <div class="terminal-line"><span class="t-output">Dados → Decisões → Impacto</span></div>
    </div>
    <p class="hero-desc">
      Profissional em transição para dados com raízes em negócios, pesquisa científica e operações digitais.
      Combino rigor metodológico acadêmico com visão orientada a resultado — e acredito que a diferença
      entre dado e decisão é uma boa análise.
    </p>
    <div class="hero-actions">
      <a href="#projetos" class="btn-primary">Ver Projetos</a>
      <a href="#fale-comigo" class="btn-outline">Fale Comigo</a>
    </div>
  </div>
</div>

<!-- SOBRE -->
<section id="sobre">
  <div class="reveal">
    <div class="section-label">sobre</div>
    <h2 class="section-title">Quem sou eu</h2>
    <div class="section-divider"></div>
  </div>
  <div class="sobre-grid reveal">
    <div class="sobre-text">
      {% for p in d.sobre %}
      <p>{{ p }}</p>
      {% endfor %}
    </div>
    <div class="sobre-stats">
      {% for s in d.stats %}
      <div class="stat-card">
        <div class="stat-value">{{ s.valor }}</div>
        <div class="stat-label">{{ s.label }}</div>
      </div>
      {% endfor %}
    </div>
  </div>
</section>

<!-- COMPETÊNCIAS -->
<section id="competencias">
  <div class="reveal">
    <div class="section-label">competências</div>
    <h2 class="section-title">Stack técnico</h2>
    <div class="section-divider"></div>
  </div>
  <div class="skills-grid">
    {% for c in d.competencias %}
    <div class="skill-category reveal">
      <div class="skill-cat-icon">{{ c.icone }}</div>
      <div class="skill-cat-name">{{ c.nome }}</div>
      <div class="skill-tags">
        {% for t in c.tags %}<span class="tag">{{ t }}</span>{% endfor %}
      </div>
    </div>
    {% endfor %}
  </div>
</section>

<!-- EXPERIÊNCIA -->
<section id="experiencia">
  <div class="reveal">
    <div class="section-label">experiência</div>
    <h2 class="section-title">Trajetória profissional</h2>
    <div class="section-divider"></div>
  </div>
  <div class="exp-timeline">
    {% for e in d.experiencias %}
    <div class="exp-item reveal">
      <div class="exp-role">{{ e.cargo }}</div>
      <div class="exp-company">{{ e.empresa }}</div>
      <ul class="exp-list">
        {% for a in e.atividades %}<li>{{ a }}</li>{% endfor %}
      </ul>
      <div class="exp-chips">
        {% for ch in e.chips %}<span class="chip">{{ ch }}</span>{% endfor %}
      </div>
    </div>
    {% endfor %}
  </div>
</section>

<!-- PROJETOS -->
<section id="projetos">
  <div class="reveal">
    <div class="section-label">projetos</div>
    <h2 class="section-title">O que já construí</h2>
    <div class="section-divider"></div>
  </div>
  <div class="projects-grid">
    {% for p in d.projetos %}
    <div class="project-card reveal">
      <div class="project-type">{{ p.tipo }}</div>
      <div class="project-name">{{ p.nome }}</div>
      <div class="project-desc">{{ p.desc }}</div>
      <div class="skill-tags">
        {% for t in p.tags %}<span class="tag">{{ t }}</span>{% endfor %}
      </div>
    </div>
    {% endfor %}
  </div>
</section>

<!-- PESQUISA -->
<section id="pesquisa">
  <div class="reveal">
    <div class="section-label">pesquisa acadêmica</div>
    <h2 class="section-title">Projeto de Mestrado</h2>
    <div class="section-divider"></div>
  </div>
  <div class="research-card reveal">
    <div>
      <div class="research-title">{{ d.pesquisa.titulo }}</div>
      <div class="research-question">{{ d.pesquisa.pergunta }}</div>
      <p class="research-desc">{{ d.pesquisa.descricao }}</p>
      <div class="status-badge">
        <div class="status-dot"></div>
        {{ d.pesquisa.status }}
      </div>
    </div>
    <div class="research-meta">
      <h4>Metodologia</h4>
      <ul>{% for m in d.pesquisa.metodologia %}<li>{{ m }}</li>{% endfor %}</ul>
      <h4>Pipeline Analítico</h4>
      <ul>{% for p in d.pesquisa.pipeline %}<li>{{ p }}</li>{% endfor %}</ul>
      <h4>Ferramentas</h4>
      <div class="skill-tags" style="margin-top:.4rem">
        {% for f in d.pesquisa.ferramentas %}<span class="tag">{{ f }}</span>{% endfor %}
      </div>
    </div>
  </div>
</section>

<!-- CONTATO -->
<section id="contato">
  <div class="reveal">
    <div class="section-label">contatos</div>
    <h2 class="section-title">Vamos conversar</h2>
  </div>
  <p class="contact-subtitle reveal">
    Aberta a oportunidades em Dados, ouvir sobre projetos interessantes
    ou simplesmente trocar ideias sobre análise e pesquisa.
  </p>
  <div class="contact-links reveal">
    <a href="{{ d.contatos.linkedin }}" target="_blank" class="contact-btn">
      <svg viewBox="0 0 24 24"><path d="M20.447 20.452h-3.554v-5.569c0-1.328-.027-3.037-1.852-3.037-1.853 0-2.136 1.445-2.136 2.939v5.667H9.351V9h3.414v1.561h.046c.477-.9 1.637-1.85 3.37-1.85 3.601 0 4.267 2.37 4.267 5.455v6.286zM5.337 7.433a2.062 2.062 0 0 1-2.063-2.065 2.064 2.064 0 1 1 2.063 2.065zm1.782 13.019H3.555V9h3.564v11.452zM22.225 0H1.771C.792 0 0 .774 0 1.729v20.542C0 23.227.792 24 1.771 24h20.451C23.2 24 24 23.227 24 22.271V1.729C24 .774 23.2 0 22.222 0h.003z"/></svg>
      LinkedIn
    </a>
    <a href="{{ d.contatos.github }}" target="_blank" class="contact-btn">
      <svg viewBox="0 0 24 24"><path d="M12 .297c-6.63 0-12 5.373-12 12 0 5.303 3.438 9.8 8.205 11.385.6.113.82-.258.82-.577 0-.285-.01-1.04-.015-2.04-3.338.724-4.042-1.61-4.042-1.61C4.422 18.07 3.633 17.7 3.633 17.7c-1.087-.744.084-.729.084-.729 1.205.084 1.838 1.236 1.838 1.236 1.07 1.835 2.809 1.305 3.495.998.108-.776.417-1.305.76-1.605-2.665-.3-5.466-1.332-5.466-5.93 0-1.31.465-2.38 1.235-3.22-.135-.303-.54-1.523.105-3.176 0 0 1.005-.322 3.3 1.23.96-.267 1.98-.399 3-.405 1.02.006 2.04.138 3 .405 2.28-1.552 3.285-1.23 3.285-1.23.645 1.653.24 2.873.12 3.176.765.84 1.23 1.91 1.23 3.22 0 4.61-2.805 5.625-5.475 5.92.42.36.81 1.096.81 2.22 0 1.606-.015 2.896-.015 3.286 0 .315.21.69.825.57C20.565 22.092 24 17.592 24 12.297c0-6.627-5.373-12-12-12"/></svg>
      GitHub
    </a>
    <a href="{{ d.contatos.email }}" class="contact-btn">
      <svg viewBox="0 0 24 24"><path d="M24 5.457v13.909c0 .904-.732 1.636-1.636 1.636h-3.819V11.73L12 16.64l-6.545-4.91v9.273H1.636A1.636 1.636 0 0 1 0 19.366V5.457c0-2.023 2.309-3.178 3.927-1.964L5.455 4.64 12 9.548l6.545-4.908 1.528-1.147C21.69 2.28 24 3.434 24 5.457z"/></svg>
      E-mail
    </a>
    <a href="{{ d.contatos.whatsapp }}" target="_blank" class="contact-btn">
      <svg viewBox="0 0 24 24"><path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51a12.8 12.8 0 0 0-.57-.01c-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 0 1-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 0 1-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 0 1 2.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0 0 12.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 0 0 5.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 0 0-3.48-8.413Z"/></svg>
      WhatsApp
    </a>
  </div>
</section>

<!-- FALE COMIGO -->
<div id="fale-comigo">
  <div>
    <div class="reveal" style="text-align:center; margin-bottom:2.5rem;">
      <div class="section-label" style="text-align:center;">fale comigo</div>
      <h2 class="form-title">Envie uma mensagem</h2>
      <p style="color:var(--text-secondary); font-size:.9rem; margin-top:.5rem;">Responderei assim que possível.</p>
    </div>
    <div class="reveal">
      <div class="form-group">
        <label for="nome">Nome</label>
        <input type="text" id="nome" placeholder="Seu nome completo"/>
      </div>
      <div class="form-group">
        <label for="email">E-mail</label>
        <input type="email" id="email" placeholder="seu@email.com"/>
      </div>
      <div class="form-group">
        <label for="assunto">Assunto</label>
        <input type="text" id="assunto" placeholder="Do que se trata?"/>
      </div>
      <div class="form-group">
        <label for="mensagem">Mensagem</label>
        <textarea id="mensagem" placeholder="Escreva sua mensagem..."></textarea>
      </div>
      <button class="btn-primary" onclick="enviarMensagem()">Enviar Mensagem</button>
      <div id="msg-feedback"></div>
    </div>
  </div>
</div>

<footer>
  <span>fgm</span>.py — {{ d.nome }} · {{ d.localizacao }} ·
  Feito com dados, intenção e um pouco de Python.
</footer>

<script>
  // Scroll reveal
  const io = new IntersectionObserver(entries => {
    entries.forEach(e => { if(e.isIntersecting){ e.target.classList.add('visible'); io.unobserve(e.target); } });
  }, { threshold: 0.12 });
  document.querySelectorAll('.reveal').forEach(el => io.observe(el));

  // Formulário → Flask
  async function enviarMensagem() {
    const nome     = document.getElementById('nome').value.trim();
    const email    = document.getElementById('email').value.trim();
    const assunto  = document.getElementById('assunto').value.trim();
    const mensagem = document.getElementById('mensagem').value.trim();
    const fb = document.getElementById('msg-feedback');

    if (!nome || !email || !mensagem) {
      fb.style.display = 'block';
      fb.style.color = '#F87171';
      fb.textContent = '>>> Preencha nome, e-mail e mensagem.';
      return;
    }

    const res = await fetch('/contato', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ nome, email, assunto, mensagem })
    });
    const data = await res.json();

    fb.style.display = 'block';
    if (data.ok) {
      fb.style.color = '#86EFAC';
      fb.textContent = '>>> Mensagem recebida. Obrigada pelo contato!';
      ['nome','email','assunto','mensagem'].forEach(id => document.getElementById(id).value = '');
    } else {
      fb.style.color = '#F87171';
      fb.textContent = '>>> Algo deu errado. Tente novamente.';
    }
  }
</script>
</body>
</html>"""


# ─────────────────────────────────────────────
#  ROTAS
# ─────────────────────────────────────────────

@app.route("/")
def index():
    return render_template_string(HTML, d=type("D", (), DADOS)())


@app.route("/contato", methods=["POST"])
def contato():
    """
    Recebe o formulário de contato via JSON.
    Por padrão apenas imprime no terminal.
    Para enviar e-mail de verdade, integre Flask-Mail ou smtplib aqui.
    """
    dados = request.get_json()
    print("\n📬 Nova mensagem recebida:")
    print(f"   De:      {dados.get('nome')} <{dados.get('email')}>")
    print(f"   Assunto: {dados.get('assunto')}")
    print(f"   Mensagem:\n   {dados.get('mensagem')}\n")
    return jsonify({"ok": True})


# ─────────────────────────────────────────────
#  INICIALIZAÇÃO
# ─────────────────────────────────────────────

if __name__ == "__main__":
    print("=" * 50)
    print("  Portfólio — Fabiola Gremski Mika")
    print("  Acesse: http://localhost:5000")
    print("=" * 50)
    app.run(debug=True, port=5000)