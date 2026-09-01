---
layout: page
permalink: /gallery/
title: Gallery
nav: true
nav_order: 8
---

<div class="container py-4">
  <!-- Intro Text -->
  <p class="lead text-muted mb-5" style="font-size: 1.1rem; line-height: 1.6;">
    Memories from the Road: Across Countries and Conferences
  </p>

  <!-- Gallery List -->
  <div class="gallery-timeline">

    <!-- IJCAI 2026 -->
    <div class="card mb-5 border-0 shadow-sm" style="background-color: var(--global-card-bg-color); border-radius: 16px; transition: transform 0.3s ease;">
      <div class="card-body p-4 p-md-5">
        <div class="d-flex flex-wrap align-items-center justify-content-between mb-3">
          <h3 class="card-title font-weight-bold mb-0" style="color: var(--global-theme-color); font-size: 1.6rem;">IJCAI 2026</h3>
          <span class="badge font-weight-bold mt-2 mt-sm-0" style="background-color: var(--global-theme-color); color: #fff; font-size: 0.85rem; padding: 6px 14px; border-radius: 20px;">Bremen, Germany</span>
        </div>
        <p class="card-text mb-4" style="font-size: 1.05rem; color: var(--global-text-color); font-style: italic;">
          <i class="fa-solid fa-quote-left mr-2" style="color: var(--global-theme-color); opacity: 0.6;"></i>
          Co-organized the Workshop on Foundation Models for Social Good (<a href="https://nlp4social.github.io/NSG-2026/" target="_blank" rel="noopener noreferrer">https://nlp4social.github.io/NSG-2026/</a>)
        </p>
        <div class="row">
          {% assign ijcai2026_files = site.static_files | where_exp: "item", "item.path contains '/assets/img/gallery/ijcai2026_'" %}
          {% for file in ijcai2026_files %}
          <div class="col-md-4 mb-4">
            <div class="gallery-item-container shadow-sm position-relative overflow-hidden" style="border-radius: 12px; height: 210px; background: var(--global-bg-color); border: 1px solid var(--global-divider-color);">
              <img src="{{ file.path | relative_url }}"
                   class="w-100 h-100 position-absolute"
                   alt="IJCAI 2026 Photo"
                   style="object-fit: contain; object-position: center; transition: transform 0.4s ease; top: 0; left: 0;"
                   onmouseover="this.style.transform='scale(1.05)'"
                   onmouseout="this.style.transform='scale(1)'">
            </div>
          </div>
          {% endfor %}
        </div>
      </div>
    </div>

    <!-- ACL 2026 -->
    <div class="card mb-5 border-0 shadow-sm" style="background-color: var(--global-card-bg-color); border-radius: 16px; transition: transform 0.3s ease;">
      <div class="card-body p-4 p-md-5">
        <div class="d-flex flex-wrap align-items-center justify-content-between mb-3">
          <h3 class="card-title font-weight-bold mb-0" style="color: var(--global-theme-color); font-size: 1.6rem;">ACL 2026</h3>
          <span class="badge font-weight-bold mt-2 mt-sm-0" style="background-color: var(--global-theme-color); color: #fff; font-size: 0.85rem; padding: 6px 14px; border-radius: 20px;">San Diego, US</span>
        </div>
        <p class="card-text mb-4" style="font-size: 1.05rem; color: var(--global-text-color); font-style: italic;">
          <i class="fa-solid fa-quote-left mr-2" style="color: var(--global-theme-color); opacity: 0.6;"></i>
          Presented two papers at ACL: "MLingualFC: Evaluating Jailbreak Vulnerabilities in Multilingual Vision-Language Models" and "TinyAttack: Exploring Stylistic Vulnerabilities in Large Language Models"
        </p>
        <div class="row">
          {% assign acl2026_files = site.static_files | where_exp: "item", "item.path contains '/assets/img/gallery/acl2026_'" %}
          {% for file in acl2026_files %}
          <div class="col-md-4 mb-4">
            <div class="gallery-item-container shadow-sm position-relative overflow-hidden" style="border-radius: 12px; height: 210px; background: var(--global-bg-color); border: 1px solid var(--global-divider-color);">
              <img src="{{ file.path | relative_url }}"
                   class="w-100 h-100 position-absolute"
                   alt="ACL 2026 Photo"
                   style="object-fit: contain; object-position: center; transition: transform 0.4s ease; top: 0; left: 0;"
                   onmouseover="this.style.transform='scale(1.05)'"
                   onmouseout="this.style.transform='scale(1)'">
            </div>
          </div>
          {% endfor %}
        </div>
      </div>
    </div>

    <!-- King's Informatics Industry Showcase -->
    <div class="card mb-5 border-0 shadow-sm" style="background-color: var(--global-card-bg-color); border-radius: 16px; transition: transform 0.3s ease;">
      <div class="card-body p-4 p-md-5">
        <div class="d-flex flex-wrap align-items-center justify-content-between mb-3">
          <h3 class="card-title font-weight-bold mb-0" style="color: var(--global-theme-color); font-size: 1.6rem;">King's Informatics Industry Showcase</h3>
          <span class="badge font-weight-bold mt-2 mt-sm-0" style="background-color: var(--global-theme-color); color: #fff; font-size: 0.85rem; padding: 6px 14px; border-radius: 20px;">London</span>
        </div>
        <p class="card-text mb-4" style="font-size: 1.05rem; color: var(--global-text-color); font-style: italic;">
          <i class="fa-solid fa-quote-left mr-2" style="color: var(--global-theme-color); opacity: 0.6;"></i>
          Presented poster "Towards Robust and Trustworthy NLP Systems"
        </p>
        <div class="row">
          {% assign kcl_showcase_files = site.static_files | where_exp: "item", "item.path contains '/assets/img/gallery/kcl_showcase_'" %}
          {% for file in kcl_showcase_files %}
          <div class="col-md-4 mb-4">
            <div class="gallery-item-container shadow-sm position-relative overflow-hidden" style="border-radius: 12px; height: 210px; background: var(--global-bg-color); border: 1px solid var(--global-divider-color);">
              <img src="{{ file.path | relative_url }}"
                   class="w-100 h-100 position-absolute"
                   alt="King's Informatics Industry Showcase Photo"
                   style="object-fit: contain; object-position: center; transition: transform 0.4s ease; top: 0; left: 0;"
                   onmouseover="this.style.transform='scale(1.05)'"
                   onmouseout="this.style.transform='scale(1)'">
            </div>
          </div>
          {% endfor %}
        </div>
      </div>
    </div>

    <!-- EACL 2026 -->
    <div class="card mb-5 border-0 shadow-sm" style="background-color: var(--global-card-bg-color); border-radius: 16px; transition: transform 0.3s ease;">
      <div class="card-body p-4 p-md-5">
        <div class="d-flex flex-wrap align-items-center justify-content-between mb-3">
          <h3 class="card-title font-weight-bold mb-0" style="color: var(--global-theme-color); font-size: 1.6rem;">EACL 2026</h3>
          <span class="badge font-weight-bold mt-2 mt-sm-0" style="background-color: var(--global-theme-color); color: #fff; font-size: 0.85rem; padding: 6px 14px; border-radius: 20px;">Rabat, Morocco</span>
        </div>
        <p class="card-text mb-4" style="font-size: 1.05rem; color: var(--global-text-color); font-style: italic;">
          <i class="fa-solid fa-quote-left mr-2" style="color: var(--global-theme-color); opacity: 0.6;"></i>
          Presented two papers at VarDial: <a href="https://aclanthology.org/2026.vardial-1.24/" target="_blank" rel="noopener noreferrer">"Improving Dialect Robustness in Large Language Models via LoRA and Mixture-of-Experts"</a> and <a href="https://aclanthology.org/2026.vardial-1.14/" target="_blank" rel="noopener noreferrer">"Indic-TunedLens: Interpreting Multilingual Models in Indian Languages"</a>
        </p>
                <div class="row">
          {% assign eacl2026_files = site.static_files | where_exp: "item", "item.path contains '/assets/img/gallery/eacl2026_'" %}
          {% for file in eacl2026_files %}
          <div class="col-md-4 mb-4">
            <div class="gallery-item-container shadow-sm position-relative overflow-hidden" style="border-radius: 12px; height: 210px; background: var(--global-bg-color); border: 1px solid var(--global-divider-color);">
              <img src="{{ file.path | relative_url }}"
                   class="w-100 h-100 position-absolute"
                   alt="EACL 2026 Photo"
                   style="object-fit: contain; object-position: center; transition: transform 0.4s ease; top: 0; left: 0;"
                   onmouseover="this.style.transform='scale(1.05)'"
                   onmouseout="this.style.transform='scale(1)'">
            </div>
          </div>
          {% endfor %}
        </div>
      </div>
    </div>

    <!-- EMNLP 2025 -->
    <div class="card mb-5 border-0 shadow-sm" style="background-color: var(--global-card-bg-color); border-radius: 16px; transition: transform 0.3s ease;">
      <div class="card-body p-4 p-md-5">
        <div class="d-flex flex-wrap align-items-center justify-content-between mb-3">
          <h3 class="card-title font-weight-bold mb-0" style="color: var(--global-theme-color); font-size: 1.6rem;">EMNLP 2025</h3>
          <span class="badge font-weight-bold mt-2 mt-sm-0" style="background-color: var(--global-theme-color); color: #fff; font-size: 0.85rem; padding: 6px 14px; border-radius: 20px;">Suzhou, China</span>
        </div>
        <p class="card-text mb-4" style="font-size: 1.05rem; color: var(--global-text-color); font-style: italic;">
          <i class="fa-solid fa-quote-left mr-2" style="color: var(--global-theme-color); opacity: 0.6;"></i>
          Presented <a href="https://aclanthology.org/2025.findings-emnlp.1208/" target="_blank" rel="noopener noreferrer">"I-GUARD: Interpretability-Guided Parameter Optimization for Adversarial Defense"</a>
        </p>
                <div class="row">
          {% assign emnlp2025_files = site.static_files | where_exp: "item", "item.path contains '/assets/img/gallery/emnlp2025_'" %}
          {% for file in emnlp2025_files %}
          <div class="col-md-4 mb-4">
            <div class="gallery-item-container shadow-sm position-relative overflow-hidden" style="border-radius: 12px; height: 210px; background: var(--global-bg-color); border: 1px solid var(--global-divider-color);">
              {% if file.path contains 'emnlp2025_2' or file.path contains 'emnlp2025_3' %}
              <img src="{{ file.path | relative_url }}"
                   class="w-100 h-100 position-absolute"
                   alt="EMNLP 2025 Photo"
                   style="object-fit: cover; object-position: center; transition: transform 0.4s ease; top: 0; left: 0;"
                   onmouseover="this.style.transform='scale(1.05)'"
                   onmouseout="this.style.transform='scale(1)'">
              {% else %}
              <img src="{{ file.path | relative_url }}"
                   class="w-100 h-100 position-absolute"
                   alt="EMNLP 2025 Photo"
                   style="object-fit: contain; object-position: center; transition: transform 0.4s ease; top: 0; left: 0;"
                   onmouseover="this.style.transform='scale(1.05)'"
                   onmouseout="this.style.transform='scale(1)'">
              {% endif %}
            </div>
          </div>
          {% endfor %}
        </div>
      </div>
    </div>

    <!-- NAACL 2025 -->
    <div class="card mb-5 border-0 shadow-sm" style="background-color: var(--global-card-bg-color); border-radius: 16px; transition: transform 0.3s ease;">
      <div class="card-body p-4 p-md-5">
        <div class="d-flex flex-wrap align-items-center justify-content-between mb-3">
          <h3 class="card-title font-weight-bold mb-0" style="color: var(--global-theme-color); font-size: 1.6rem;">NAACL 2025</h3>
          <span class="badge font-weight-bold mt-2 mt-sm-0" style="background-color: var(--global-theme-color); color: #fff; font-size: 0.85rem; padding: 6px 14px; border-radius: 20px;">Albuquerque, New Mexico</span>
        </div>
        <p class="card-text mb-4" style="font-size: 1.05rem; color: var(--global-text-color); font-style: italic;">
          <i class="fa-solid fa-quote-left mr-2" style="color: var(--global-theme-color); opacity: 0.6;"></i>
          Presented <a href="https://aclanthology.org/2025.naacl-long.534/" target="_blank" rel="noopener noreferrer">"FactEval: Evaluating the Robustness of Fact Verification Systems in the Era of Large Language Models"</a> (My first paper as Dr. Mamta.)
        </p>
                <div class="row">
          {% assign naacl2025_files = site.static_files | where_exp: "item", "item.path contains '/assets/img/gallery/naacl2025_'" %}
          {% for file in naacl2025_files %}
          <div class="col-md-4 mb-4">
            <div class="gallery-item-container shadow-sm position-relative overflow-hidden" style="border-radius: 12px; height: 210px; background: var(--global-bg-color); border: 1px solid var(--global-divider-color);">
              <img src="{{ file.path | relative_url }}"
                   class="w-100 h-100 position-absolute"
                   alt="NAACL 2025 Photo"
                   style="object-fit: contain; object-position: center; transition: transform 0.4s ease; top: 0; left: 0;"
                   onmouseover="this.style.transform='scale(1.05)'"
                   onmouseout="this.style.transform='scale(1)'">
            </div>
          </div>
          {% endfor %}
        </div>
      </div>
    </div>

    <!-- EMNLP 2024 -->
    <div class="card mb-5 border-0 shadow-sm" style="background-color: var(--global-card-bg-color); border-radius: 16px; transition: transform 0.3s ease;">
      <div class="card-body p-4 p-md-5">
        <div class="d-flex flex-wrap align-items-center justify-content-between mb-3">
          <h3 class="card-title font-weight-bold mb-0" style="color: var(--global-theme-color); font-size: 1.6rem;">EMNLP 2024</h3>
          <span class="badge font-weight-bold mt-2 mt-sm-0" style="background-color: var(--global-theme-color); color: #fff; font-size: 0.85rem; padding: 6px 14px; border-radius: 20px;">Miami, USA</span>
        </div>
        <p class="card-text mb-4" style="font-size: 1.05rem; color: var(--global-text-color); font-style: italic;">
          <i class="fa-solid fa-quote-left mr-2" style="color: var(--global-theme-color); opacity: 0.6;"></i>
          Presented <a href="https://aclanthology.org/2024.emnlp-main.1172/" target="_blank" rel="noopener noreferrer">"BiasWipe: Mitigating Unintended Bias in Text Classifiers through Model Interpretability"</a>
        </p>
                <div class="row">
          {% assign emnlp2024_files = site.static_files | where_exp: "item", "item.path contains '/assets/img/gallery/emnlp2024_'" %}
          {% for file in emnlp2024_files %}
          <div class="col-md-4 mb-4">
            <div class="gallery-item-container shadow-sm position-relative overflow-hidden" style="border-radius: 12px; height: 210px; background: var(--global-bg-color); border: 1px solid var(--global-divider-color);">
              <img src="{{ file.path | relative_url }}"
                   class="w-100 h-100 position-absolute"
                   alt="EMNLP 2024 Photo"
                   style="object-fit: contain; object-position: center; transition: transform 0.4s ease; top: 0; left: 0;"
                   onmouseover="this.style.transform='scale(1.05)'"
                   onmouseout="this.style.transform='scale(1)'">
            </div>
          </div>
          {% endfor %}
        </div>
      </div>
    </div>

    <!-- EMNLP 2023 -->
    <div class="card mb-5 border-0 shadow-sm" style="background-color: var(--global-card-bg-color); border-radius: 16px; transition: transform 0.3s ease;">
      <div class="card-body p-4 p-md-5">
        <div class="d-flex flex-wrap align-items-center justify-content-between mb-3">
          <h3 class="card-title font-weight-bold mb-0" style="color: var(--global-theme-color); font-size: 1.6rem;">EMNLP 2023</h3>
          <span class="badge font-weight-bold mt-2 mt-sm-0" style="background-color: var(--global-theme-color); color: #fff; font-size: 0.85rem; padding: 6px 14px; border-radius: 20px;">Singapore</span>
        </div>
        <p class="card-text mb-4" style="font-size: 1.05rem; color: var(--global-text-color); font-style: italic;">
          <i class="fa-solid fa-quote-left mr-2" style="color: var(--global-theme-color); opacity: 0.6;"></i>
          Presented <a href="https://aclanthology.org/2023.emnlp-main.987/" target="_blank" rel="noopener noreferrer">"Elevating Code-mixed Text Handling through Auditory Information of Words"</a>
        </p>
                <div class="row">
          {% assign emnlp2023_files = site.static_files | where_exp: "item", "item.path contains '/assets/img/gallery/emnlp2023_'" %}
          {% for file in emnlp2023_files %}
          <div class="col-md-4 mb-4">
            <div class="gallery-item-container shadow-sm position-relative overflow-hidden" style="border-radius: 12px; height: 210px; background: var(--global-bg-color); border: 1px solid var(--global-divider-color);">
              <img src="{{ file.path | relative_url }}"
                   class="w-100 h-100 position-absolute"
                   alt="EMNLP 2023 Photo"
                   style="object-fit: contain; object-position: center; transition: transform 0.4s ease; top: 0; left: 0;"
                   onmouseover="this.style.transform='scale(1.05)'"
                   onmouseout="this.style.transform='scale(1)'">
            </div>
          </div>
          {% endfor %}
        </div>
      </div>
    </div>

    <!-- ECIR 2023 -->
    <div class="card mb-5 border-0 shadow-sm" style="background-color: var(--global-card-bg-color); border-radius: 16px; transition: transform 0.3s ease;">
      <div class="card-body p-4 p-md-5">
        <div class="d-flex flex-wrap align-items-center justify-content-between mb-3">
          <h3 class="card-title font-weight-bold mb-0" style="color: var(--global-theme-color); font-size: 1.6rem;">ECIR 2023</h3>
          <span class="badge font-weight-bold mt-2 mt-sm-0" style="background-color: var(--global-theme-color); color: #fff; font-size: 0.85rem; padding: 6px 14px; border-radius: 20px;">Dublin, Ireland</span>
        </div>
        <p class="card-text mb-4" style="font-size: 1.05rem; color: var(--global-text-color); font-style: italic;">
          <i class="fa-solid fa-quote-left mr-2" style="color: var(--global-theme-color); opacity: 0.6;"></i>
          Presented <a href="https://link.springer.com/chapter/10.1007/978-3-031-28244-7_43" target="_blank" rel="noopener noreferrer">"Service is Good, Very Good or Excellent? Towards Aspect-Based Sentiment Intensity Analysis"</a> (my first international travel.)
        </p>
                <div class="row">
          {% assign ecir2023_files = site.static_files | where_exp: "item", "item.path contains '/assets/img/ecir2023_'" %}
          {% for file in ecir2023_files %}
          <div class="col-md-4 mb-4">
            <div class="gallery-item-container shadow-sm position-relative overflow-hidden" style="border-radius: 12px; height: 210px; background: var(--global-bg-color); border: 1px solid var(--global-divider-color);">
              <img src="{{ file.path | relative_url }}"
                   class="w-100 h-100 position-absolute"
                   alt="ECIR 2023 Photo"
                   style="object-fit: cover; object-position: center; transition: transform 0.4s ease; top: 0; left: 0;"
                   onmouseover="this.style.transform='scale(1.05)'"
                   onmouseout="this.style.transform='scale(1)'">
            </div>
          </div>
          {% endfor %}
        </div>
      </div>
    </div>

  </div>
</div>
