---
layout: archive
title: "Research Experience"
permalink: /research/
author_profile: true
redirect_from: /research.html
---

<h2>Heterogeneity of single-cell Hi-C DNA data Analysis</h2>
<p><em>March 2024 - Present, University of Toronto, Toronto, Canada</em></p>
<div style="display: flex;">
  <div style="position: relative; margin-right: 20px;">
    <img id="staticGif1" src="../images/rotating_cells.png" alt="Single Cell Hi-C" style="max-width: 225px; height: auto;" />
    <img id="animatedGif1" src="../images/rotating_cells.gif" alt="Single Cell Hi-C Animated" style="max-width: 225px; height: auto; display: none;" />
  </div>
  <div>
    <p> This research focuses on the heterogeneity of single-cell Hi-C DNA data to explore the quantitative methods for classifying different types of single cells based on DNA Hi-C data and contact matrices. Large amount of data cleaning and transformation is performed on the original dataset, different methods of dimension reduction are applied, including Principle Component Analysis, t-SNE, UMAP, with clustering techniques such as K-Means performed on lower dimension representations.</p>
    <p><em>Supervisor:</em> Professor. Elena Tuzhilina</p>
  </div>
</div>
<hr/>

<h2>Multi-agent LLM for Mental Health Diagnosis</h2>
<p><em>April 2024 - August 2024, University of Toronto, Toronto, Canada</em></p>
<div style="display: flex;">
  <div style="position: relative; margin-right: 20px;">
    <img id="staticGif2" src="../images/llm_score.png" alt="llm score" style="max-width: 225px; height: auto;" />
    <img id="animatedGif2" src="../images/llm_score.gif" alt="llm score Animated" style="max-width: 225px; height: auto; display: none;" />
  </div>
  <div>
  <p> This project involves the development of a multi-agent framework using LLMs to simulate a therapist's role in mental health diagnosis. The goal is to establish a framework that can mimic a therapist by interacting with users and analyzing responses to provide insights into their mental health. My contributions to this project included working on both the backend and frontend development, as well as the prompt engineering for the models. I also conducted experiments to evaluate the performance of the models and the overall system.</p>

  <p><em>Supervisors:</em> Bill Yuanhong Sun, Professor. Kang Lee</p>
  <a href="https://drive.google.com/file/d/1pGTPmJ7qZWFp33U70Gwz5icv3kAia4kr/view?usp=drive_link">Demo Video</a>
  </div>
</div>
<hr/>

<h2>Multi-class Anxiety Prediction Approximation for Long Assessments</h2>
<p><em>April 2024 - August 2024, University of Toronto, Toronto, Canada</em></p>

<div style="display: flex;">
    <img src="../images/shap_summary.png" alt="shap" align="left" style="width: 225px; height: 225px; margin-right: 20px;" />
    <div>
        <p>This research introduces a novel approach for predicting multi-class anxiety levels through a machine learning framework designed to handle long assessments. We developed a model that shortens lengthy assessments while maintaining high accuracy. This approach demonstrated robust performance through validations, highlighting potentials for practical application in clinical and research settings. This study shows the importance of using machine learning models to enhance the efficiency and accuracy of mental health analysis.</p>
        <p><em>Supervisors:</em> Bill Yuanhong Sun, Professor. Kang Lee</p>
        <a href="../files/Rogers SUDS Poster.pdf">Poster</a>
    </div>
</div>

<hr/>

<h2>Leaky Emotion in Social Psychology by Reinforcement Learning</h2>
<p><em>September 2023 – May 2024, University of Toronto, Toronto, Canada</em></p>
<div style="display: flex;">
  <div style="position: relative; margin-right: 20px;">
    <img id="staticGif3" src="../images/ani.png" alt="llm score" style="max-width: 225px; height: auto;" />
    <img id="animatedGif3" src="../images/ani.gif" alt="llm score Animated" style="max-width: 225px; height: auto; display: none;" />
  </div>
  <div>
    <p> This project explores the impact of emotions on the behavior of agents in a social setting using reinforcement learning. The study employs a gaming environment where agents share information about the location of wolves to avoid predation. By fine-tuning the model, the research aims to show how leaked emotions through communication can enhance benefit among agents. Key tasks included designing visuals for the training process, optimizing game logic, and apply heatmaps to validate various social cognition theories.</p>
    <p><em>Supervisor:</em> Professor. William Cunningham</p>
  </div>
</div>
<hr/>

<h2>Real-Life Data Modeling with the Modified Burr III Odds Ratio–G Distribution</h2>
<p><em>September 2023 – May 2024, University of West Florida, Pensacola, USA</em></p>
<div style="display: flex;">
  <img src="../images/burrIII.png" alt="BurrIII" align="left" style="width: 225px; height: 225px; margin-right: 20px;" />
  <div>
    <p> This research presents the modified Burr III Odds Ratio–G distribution, a novel model that integrates odds ratio with Burr III distribution. Focusing on the Burr III Scaled Inverse Odds Ratio–G subclass, this model enhances flexibility and predictive accuracy. The study explores the mathematical properties of the distribution, including hazard rates, quantiles, and moments by proofs. Rigorous simulations confirm the robustness of the model, and its application to datasets demonstrates its efficacy compared to established distributions.</p>
    <p><em>Supervisor:</em> Professor. Shusen Pu</p>
    <a href="../files/axioms-13-00401-v2.pdf">Paper</a>
  </div>
<div>

<script>
  document.addEventListener("DOMContentLoaded", function() {
    const imagePairs = [
      { static: 'staticGif1', animated: 'animatedGif1' },
      { static: 'staticGif2', animated: 'animatedGif2' },
      { static: 'staticGif3', animated: 'animatedGif3' }
    ];

    imagePairs.forEach(pair => {
      const staticGif = document.getElementById(pair.static);
      const animatedGif = document.getElementById(pair.animated);

      staticGif.addEventListener("mouseover", function() {
        staticGif.style.display = "none";
        animatedGif.style.display = "block";
      });

      animatedGif.addEventListener("mouseout", function() {
        animatedGif.style.display = "none";
        staticGif.style.display = "block";
      });
    });
  });
</script>