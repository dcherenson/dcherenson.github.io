---
layout: default
title: "Home"
---

<!-- Page Container -->
<div style="position: relative;">

  <!-- Background Video -->
  <!-- <video autoplay muted loop playsinline
         style="position: fixed; top: 0; left: 0; width: 100vw; height: 100vh;
                object-fit: cover; z-index: 0;">
    <source src="/pics/vid2.mp4" type="video/mp4">
  </video> -->

  <!-- Foreground Content -->
  <div style="position: relative; z-index: 1; display: flex; flex-direction: column; align-items: center; padding: 60px 20px;">

    <!-- Profile Card -->
    <div style="display: flex; flex-direction: column; align-items: center; text-align: center; 
                padding: 25px; max-width: 400px; border-radius: 14px;
                box-shadow: 0 6px 20px rgba(0,0,0,0.12); background-color: rgba(255,255,255,0.85);
                transition: transform 0.3s; margin-top: 80px;">
      
      <img src="/pics/cherenson_headshot.jpg" 
           alt="Daniel Cherenson, PhD Student in Robotics" 
           style="width: 180px; height: 180px; border-radius: 50%; object-fit: cover; margin-bottom: 15px;">

      <h1 style="margin: 0; font-size: 1.9rem;"><strong>Daniel Cherenson</strong></h1>
      <p style="margin: 6px 0 15px 0; font-size: 1rem; color: #555;">
        <strong>PhD Student</strong> in Robotics, University of Michigan
      </p>

      <div style="font-size: 0.95rem; color: #444; line-height: 1.6;">
        📧 <a href="mailto:dmrc@umich.edu">dmrc@umich.edu</a><br>
        🔗 <a href="https://scholar.google.com/citations?user=a87kck4AAAAJ&hl=en" target="_blank">Google Scholar</a> · 
           <a href="https://github.com/dcherenson/" target="_blank">GitHub</a> · 
           <a href="https://www.linkedin.com/in/dcherenson/" target="_blank">LinkedIn</a>
      </div>
    </div>

    <!-- Bio Section -->
    <div style="max-width: 800px; margin-top: 40px; line-height: 1.7; font-size: 1rem; color: #333; background-color: rgba(255,255,255,0.85); padding: 20px; border-radius: 14px;">
      <p>
      I am a second-year Ph.D student at the
      <a href="https://dasc-lab.github.io/" target="_blank">DASC Lab</a>, part of the 
      <a href="https://robotics.umich.edu/" target="_blank">Department of Robotics</a> at the University of Michigan, Ann Arbor. 
      I am advised by <a href="https://websites.umich.edu/~dpanagou/" target="_blank">Professor Dimitra Panagou</a>. 
      My research interests are safe and efficient planning and control under uncertainty with applications to aerial robotic systems.
      </p>

      <p>
        Previously, I was a guidance, navigation, and control (GNC) engineer at Raytheon, L3Harris, and Near Earth Autonomy, where I worked on missile guidance, hypersonic vehicle simulation, VTOL control, and GPS-denied navigation. I received an MS in Electrical Engineering and a BS in Mechanical Engineering from 
        <a href="https://ese.washu.edu/index.html" target="_blank">Washington University in St. Louis</a>.
      </p>
    </div>

  </div>
</div>

<style>
  /* Hover effect for profile card */
  .profile-card:hover {
    transform: translateY(-5px);
  }

  /* Ensure responsive stacking */
  @media (max-width: 768px) {
    .profile-card, .bio-section {
      width: 90%;
    }
  }
</style>
