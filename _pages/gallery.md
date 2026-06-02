---
layout: page
permalink: /gallery/
title: Gallery
description: Photos and memories from various international conferences and academic events.
nav: true
nav_order: 8
---

<div class="container py-4">
  <!-- Intro Text -->
  <p class="lead text-muted mb-5" style="font-size: 1.1rem; line-height: 1.6;">
    A visual collection of memories, research presentations, and academic journeys from key conferences and collaborations around the world.
  </p>

  <!-- Gallery List -->
  <div class="gallery-timeline">

    <!-- EACL 2026 -->
    <div class="card mb-5 border-0 shadow-sm" style="background-color: var(--global-card-bg-color); border-radius: 16px; transition: transform 0.3s ease;">
      <div class="card-body p-4 p-md-5">
        <div class="d-flex flex-wrap align-items-center justify-content-between mb-3">
          <h3 class="card-title font-weight-bold mb-0" style="color: var(--global-theme-color); font-size: 1.6rem;">EACL 2026</h3>
          <span class="badge font-weight-bold mt-2 mt-sm-0" style="background-color: var(--global-theme-color); color: #fff; font-size: 0.85rem; padding: 6px 14px; border-radius: 20px;">Rabat, Morocco</span>
        </div>
        <p class="card-text mb-4" style="font-size: 1.05rem; color: var(--global-text-color); font-style: italic;">
          <i class="fa-solid fa-quote-left mr-2" style="color: var(--global-theme-color); opacity: 0.6;"></i>
          Presented two papers at VarDial
        </p>
        <div class="row">
          {% for i in (1..3) %}
          <div class="col-md-4 mb-4">
            <div class="gallery-item-container shadow-sm position-relative overflow-hidden" style="border-radius: 12px; height: 210px; background: var(--global-bg-color); border: 1px solid var(--global-divider-color);">
              <img src="{{ '/assets/img/gallery/eacl2026_' | append: i | append: '.jpg' | relative_url }}"
                   class="w-100 h-100 position-absolute"
                   alt="EACL 2026 Photo {{ i }}"
                   style="object-fit: cover; object-position: center; display: none; transition: transform 0.4s ease; top: 0; left: 0;"
                   onload="this.style.display='block'; this.nextElementSibling.style.display='none'; this.parentElement.style.borderStyle='solid';"
                   onerror="this.style.display='none'; this.nextElementSibling.style.display='flex';"
                   onmouseover="this.style.transform='scale(1.05)'"
                   onmouseout="this.style.transform='scale(1)'">

              <div class="gallery-placeholder d-flex flex-column align-items-center justify-content-center w-100 h-100 p-3 text-center"
                   style="border: 2px dashed var(--global-theme-color); border-radius: 12px; background: var(--global-card-bg-color); opacity: 0.85; transition: all 0.3s ease;">
                <i class="fa-regular fa-image mb-2" style="font-size: 2.2rem; color: var(--global-theme-color); opacity: 0.7;"></i>
                <span style="font-size: 0.85rem; font-weight: 600; color: var(--global-text-color);">Photo {{ i }}</span>
                <small class="text-muted" style="font-size: 0.7rem; margin-top: 5px; word-break: break-all;">assets/img/gallery/eacl2026_{{ i }}.jpg</small>
              </div>
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
          Presented I-GUARD
        </p>
        <div class="row">
          {% for i in (1..3) %}
          <div class="col-md-4 mb-4">
            <div class="gallery-item-container shadow-sm position-relative overflow-hidden" style="border-radius: 12px; height: 210px; background: var(--global-bg-color); border: 1px solid var(--global-divider-color);">
              <img src="{{ '/assets/img/gallery/emnlp2025_' | append: i | append: '.jpg' | relative_url }}"
                   class="w-100 h-100 position-absolute"
                   alt="EMNLP 2025 Photo {{ i }}"
                   style="object-fit: cover; object-position: center; display: none; transition: transform 0.4s ease; top: 0; left: 0;"
                   onload="this.style.display='block'; this.nextElementSibling.style.display='none'; this.parentElement.style.borderStyle='solid';"
                   onerror="this.style.display='none'; this.nextElementSibling.style.display='flex';"
                   onmouseover="this.style.transform='scale(1.05)'"
                   onmouseout="this.style.transform='scale(1)'">

              <div class="gallery-placeholder d-flex flex-column align-items-center justify-content-center w-100 h-100 p-3 text-center"
                   style="border: 2px dashed var(--global-theme-color); border-radius: 12px; background: var(--global-card-bg-color); opacity: 0.85; transition: all 0.3s ease;">
                <i class="fa-regular fa-image mb-2" style="font-size: 2.2rem; color: var(--global-theme-color); opacity: 0.7;"></i>
                <span style="font-size: 0.85rem; font-weight: 600; color: var(--global-text-color);">Photo {{ i }}</span>
                <small class="text-muted" style="font-size: 0.7rem; margin-top: 5px; word-break: break-all;">assets/img/gallery/emnlp2025_{{ i }}.jpg</small>
              </div>
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
          First paper as Dr. Mamta, FactEval
        </p>
        <div class="row">
          {% for i in (1..3) %}
          <div class="col-md-4 mb-4">
            <div class="gallery-item-container shadow-sm position-relative overflow-hidden" style="border-radius: 12px; height: 210px; background: var(--global-bg-color); border: 1px solid var(--global-divider-color);">
              <img src="{{ '/assets/img/gallery/naacl2025_' | append: i | append: '.jpg' | relative_url }}"
                   class="w-100 h-100 position-absolute"
                   alt="NAACL 2025 Photo {{ i }}"
                   style="object-fit: cover; object-position: center; display: none; transition: transform 0.4s ease; top: 0; left: 0;"
                   onload="this.style.display='block'; this.nextElementSibling.style.display='none'; this.parentElement.style.borderStyle='solid';"
                   onerror="this.style.display='none'; this.nextElementSibling.style.display='flex';"
                   onmouseover="this.style.transform='scale(1.05)'"
                   onmouseout="this.style.transform='scale(1)'">

              <div class="gallery-placeholder d-flex flex-column align-items-center justify-content-center w-100 h-100 p-3 text-center"
                   style="border: 2px dashed var(--global-theme-color); border-radius: 12px; background: var(--global-card-bg-color); opacity: 0.85; transition: all 0.3s ease;">
                <i class="fa-regular fa-image mb-2" style="font-size: 2.2rem; color: var(--global-theme-color); opacity: 0.7;"></i>
                <span style="font-size: 0.85rem; font-weight: 600; color: var(--global-text-color);">Photo {{ i }}</span>
                <small class="text-muted" style="font-size: 0.7rem; margin-top: 5px; word-break: break-all;">assets/img/gallery/naacl2025_{{ i }}.jpg</small>
              </div>
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
          Biaswipe paper
        </p>
        <div class="row">
          {% for i in (1..3) %}
          <div class="col-md-4 mb-4">
            <div class="gallery-item-container shadow-sm position-relative overflow-hidden" style="border-radius: 12px; height: 210px; background: var(--global-bg-color); border: 1px solid var(--global-divider-color);">
              <img src="{{ '/assets/img/gallery/emnlp2024_' | append: i | append: '.jpg' | relative_url }}"
                   class="w-100 h-100 position-absolute"
                   alt="EMNLP 2024 Photo {{ i }}"
                   style="object-fit: cover; object-position: center; display: none; transition: transform 0.4s ease; top: 0; left: 0;"
                   onload="this.style.display='block'; this.nextElementSibling.style.display='none'; this.parentElement.style.borderStyle='solid';"
                   onerror="this.style.display='none'; this.nextElementSibling.style.display='flex';"
                   onmouseover="this.style.transform='scale(1.05)'"
                   onmouseout="this.style.transform='scale(1)'">

              <div class="gallery-placeholder d-flex flex-column align-items-center justify-content-center w-100 h-100 p-3 text-center"
                   style="border: 2px dashed var(--global-theme-color); border-radius: 12px; background: var(--global-card-bg-color); opacity: 0.85; transition: all 0.3s ease;">
                <i class="fa-regular fa-image mb-2" style="font-size: 2.2rem; color: var(--global-theme-color); opacity: 0.7;"></i>
                <span style="font-size: 0.85rem; font-weight: 600; color: var(--global-text-color);">Photo {{ i }}</span>
                <small class="text-muted" style="font-size: 0.7rem; margin-top: 5px; word-break: break-all;">assets/img/gallery/emnlp2024_{{ i }}.jpg</small>
              </div>
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
          Elevating code-mixed...
        </p>
        <div class="row">
          {% for i in (1..3) %}
          <div class="col-md-4 mb-4">
            <div class="gallery-item-container shadow-sm position-relative overflow-hidden" style="border-radius: 12px; height: 210px; background: var(--global-bg-color); border: 1px solid var(--global-divider-color);">
              <img src="{{ '/assets/img/gallery/emnlp2023_' | append: i | append: '.jpg' | relative_url }}"
                   class="w-100 h-100 position-absolute"
                   alt="EMNLP 2023 Photo {{ i }}"
                   style="object-fit: cover; object-position: center; display: none; transition: transform 0.4s ease; top: 0; left: 0;"
                   onload="this.style.display='block'; this.nextElementSibling.style.display='none'; this.parentElement.style.borderStyle='solid';"
                   onerror="this.style.display='none'; this.nextElementSibling.style.display='flex';"
                   onmouseover="this.style.transform='scale(1.05)'"
                   onmouseout="this.style.transform='scale(1)'">

              <div class="gallery-placeholder d-flex flex-column align-items-center justify-content-center w-100 h-100 p-3 text-center"
                   style="border: 2px dashed var(--global-theme-color); border-radius: 12px; background: var(--global-card-bg-color); opacity: 0.85; transition: all 0.3s ease;">
                <i class="fa-regular fa-image mb-2" style="font-size: 2.2rem; color: var(--global-theme-color); opacity: 0.7;"></i>
                <span style="font-size: 0.85rem; font-weight: 600; color: var(--global-text-color);">Photo {{ i }}</span>
                <small class="text-muted" style="font-size: 0.7rem; margin-top: 5px; word-break: break-all;">assets/img/gallery/emnlp2023_{{ i }}.jpg</small>
              </div>
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
          Where my journey begins, my first conference
        </p>
        <div class="row">
          {% for i in (1..3) %}
          <div class="col-md-4 mb-4">
            <div class="gallery-item-container shadow-sm position-relative overflow-hidden" style="border-radius: 12px; height: 210px; background: var(--global-bg-color); border: 1px solid var(--global-divider-color);">
              <img src="{{ '/assets/img/gallery/ecir2023_' | append: i | append: '.jpg' | relative_url }}"
                   class="w-100 h-100 position-absolute"
                   alt="ECIR 2023 Photo {{ i }}"
                   style="object-fit: cover; object-position: center; display: none; transition: transform 0.4s ease; top: 0; left: 0;"
                   onload="this.style.display='block'; this.nextElementSibling.style.display='none'; this.parentElement.style.borderStyle='solid';"
                   onerror="this.style.display='none'; this.nextElementSibling.style.display='flex';"
                   onmouseover="this.style.transform='scale(1.05)'"
                   onmouseout="this.style.transform='scale(1)'">

              <div class="gallery-placeholder d-flex flex-column align-items-center justify-content-center w-100 h-100 p-3 text-center"
                   style="border: 2px dashed var(--global-theme-color); border-radius: 12px; background: var(--global-card-bg-color); opacity: 0.85; transition: all 0.3s ease;">
                <i class="fa-regular fa-image mb-2" style="font-size: 2.2rem; color: var(--global-theme-color); opacity: 0.7;"></i>
                <span style="font-size: 0.85rem; font-weight: 600; color: var(--global-text-color);">Photo {{ i }}</span>
                <small class="text-muted" style="font-size: 0.7rem; margin-top: 5px; word-break: break-all;">assets/img/gallery/ecir2023_{{ i }}.jpg</small>
              </div>
            </div>
          </div>
          {% endfor %}
        </div>
      </div>
    </div>

  </div>
</div>
