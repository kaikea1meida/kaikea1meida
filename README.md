<div align="right">
  <a href="README.md">English</a> | <a href="README-pt.md">Português</a>
</div>

<div align="center">

# Ooooii!!!


## 'Kaike Almeida'

**Computer Science Student | C Developer | Graphs & Data Structures**

[![University](https://img.shields.io/badge/UFRRJ-Computer%20Science-2e8b57?style=for-the-badge)](https://portal.ufrrj.br/)
[![Language](https://img.shields.io/badge/Language-C-00599C?style=for-the-badge&logo=c&logoColor=white)](https://en.cppreference.com/w/c)

</div>

---

## `01.` About me

Hi!! I'm **Kaike**, a Computer Science undergraduate student at **Universidade Federal Rural do Rio de Janeiro (UFRRJ - Instituto Multidisciplinar)**.

I'm currently in my **second semester**. I'm interested in learning more about computer architecture, graph theory and data structures, as well as understanding how they work and how they can be used to improve my problem-solving skills.

Most of my current studies involve projects in **C**, including algorithms for recognizing strongly chordal graphs and a game that started as an assignment for my Structured Programming classes. I'm also beginning to explore MIPS architecture.

<details>
<summary><h3><kbd><b>&nbsp;click info about me&nbsp;</b></kbd></h3></summary>

- Computer Science student at UFRRJ.
- Currently in the 2nd semester.
- Learning and developing projects in C.
- Interested in data structures, algorithms and graph theory.
- Languages: Portuguese (Brazilian) and English.
- Linux user.

</details>

<details>
<summary><h3><kbd><b>&nbsp;click - Fastfetch me!&nbsp;</b></kbd></h3></summary>

<br>

<p align="center">
  <img src="./eueu-avatar.png" alt="Avatar ASCII" width="750">
</p>

<br>

</details>

---

## `02.` Technologies & Knowledge

<div align="center">

### Languages and tools

<img src="https://skillicons.dev/icons?i=c,linux,git,github" alt="C, Linux, Git and GitHub icons">

</div>

| Area | Knowledge |
|:---|:---|
| Programming language | C |
| Data structures | Basics and implementation |
| Graph theory | Schordal graphs & algorithms |
| Operating system | Linux |
| Version control | Git & GitHub |
| Languages | Portuguese and English |

---

## `03.` Working on

### Terminal Game — C + Ncurses
<div align="center">
  <img src="./ncurses-banner.svg" alt="C + Ncurses">
</div>

I'm currently developing a game in **C**, using mainly the **Ncurses** library to create a text-based interface directly in the terminal.
<details>
  <summary><h3><kbd><b>&nbsp;click - Game info and pictures&nbsp;</b></kbd></h3></summary>
  <img width="1396" height="678" alt="Captura de tela de 2026-11-02 16-08-54" src="https://github.com/user-attachments/assets/a2494cf0-74d7-46cb-b336-68a43acb8039" />
<img width="875" height="879" alt="Captura de tela de 2026-11-02 16-12-27" src="https://github.com/user-attachments/assets/fe89d561-c332-4913-983c-4818f770309c" />
<img width="875" height="879" alt="Captura de tela de 2026-11-02 16-11-44" src="https://github.com/user-attachments/assets/2c985d23-056e-4b58-a825-47fddfc407ef" />
<img width="875" height="879" alt="Captura de tela de 2026-11-02 16-11-15" src="https://github.com/user-attachments/assets/79afab3e-f58c-46c8-9b7f-746b32b1a12c" />
<img width="1340" height="622" alt="Captura de tela de 2026-11-02 16-10-42" src="https://github.com/user-attachments/assets/bad9ac8d-861b-4cbd-a23d-c3b3fca8b136" />
<img width="1340" height="622" alt="Captura de tela de 2026-11-02 16-09-58" src="https://github.com/user-attachments/assets/708c072e-a639-4c4f-b00a-8c397728d2c0" />

</details>
The project started as an opportunity during my first semester to explore terminal-based interfaces, keyboard interaction, screen rendering and the practical application of programming concepts. It also involves working with sprites, memory loading and binary archives.

<br>

<div align="center">
  <img src="https://img.shields.io/badge/C-00599C?style=flat-square&logo=c&logoColor=white" alt="C">
  <img src="https://img.shields.io/badge/Ncurses-Terminal%20UI-222222?style=flat-square&logo=gnubash&logoColor=white" alt="Ncurses">
  <img src="https://img.shields.io/badge/Status-In%20Development-orange?style=flat-square" alt="In development">
</div>

**Documentation:** I'm also writing my own README explaining the basic concepts of Ncurses, its main functions and how to get started with the library.

About Ncurses and the in development game!

### **Ncurses.md:** **[Ncurses — Basic Concepts and Introduction](https://github.com/kaikeaes/while_playing_not_studying-OO-/blob/main/explicancurses.md)**

### **Repository:** [While Playing Not Studying — C Game](https://github.com/leoeowoeo/while_playing_not_studying-OO-)


# Strongly Chordal Graphs Library

Another project I'm working on is a library related to **strongly chordal graphs**, using graph data structures.

This project involves studying graph representations and applying data structures to work with graph-related problems.

<div align="center">
  <img src="./Matriz_Schordals.gif" alt="Adjacency Matrix - Strongly Chordal Graphs" width="650">
</div>
<br>

<div align="center">
  <img src="https://img.shields.io/badge/Language-C-00599C?style=flat-square&logo=c&logoColor=white" alt="C">
  <img src="https://img.shields.io/badge/Topic-Graph%20Theory-6A5ACD?style=flat-square" alt="Graph theory">
  <img src="https://img.shields.io/badge/Topic-Data%20Structures-2E8B57?style=flat-square" alt="Data structures">
</div>

**Repository:** [Strongly Chordal Graphs Library](https://github.com/kaikea1meida/Grafo.h)

<details>
<summary><h3><kbd><b>&nbsp;click - What is the project about?&nbsp;</b></kbd></h3></summary>

## Strongly Chordal Graph Recognition

This project recognizes whether a graph G is strongly chordal by reducing the problem to checking if its auxiliary vertex-clique graph H(G) is chordal bipartite.

We are also visualizing the graphs  trough adjacency matrices, only looking at one triangle ( superior or inferior depending on the necessity)
### Theoretical idea

A graph G is strongly chordal if and only if its vertex-clique incidence graph H(G) is chordal bipartite.

### Steps

#### 1. Building the auxiliary bipartite graph H(G) = (X ∪ Y, E)

- **Set X (original vertices):** contains all original vertices from G.
- **Set Y (cliques):** contains nodes representing each maximal clique in G.
- **Edges:** an edge connects vertex u in X to clique node C in Y if u belongs to C.

How we build it:

1. Run a Perfect Elimination Ordering (PEO) on G, so that we are sure that it is cordal at least, because looking for cliques in a non cordal graph may be NP-complete.
<details>
<summary><kbd><sub><b>&nbsp;about the gif&nbsp;</b></sub></kbd></summary>
  ##### *this image is not from our project but it represents almost exactly what we are doing here, it is from: https://oxfordcontrol.github.io/COSMO.jl/stable/decomposition/*
</details>
2. For each vertex in the PEO, take its remaining closed neighborhood.
3. Check if that neighborhood is already contained in an existing clique in Y. If it's not, add a new clique node to Y and link it to all vertices in that neighborhood.

#### 2. Bisimplicial elimination on H(G)

- Loop over the edges (u, v) in H(G), where u is in X and v is in Y.
- For each edge, check if the joint neighborhood N(u) ∪ N(v) forms a complete bipartite graph (biclique).
- If it does, pick the bisimplicial vertex (the one whose neighborhood sits entirely inside this biclique).
- Remove that vertex and all its incident edges from H(G).

#### 3. Output

- **If H(G) ends up completely empty:** G is strongly chordal.
- **If the loop gets stuck and can't find any bisimplicial vertices:** G is not strongly chordal.

</details>

---

## `04.` GitHub Statistics

<div align="center">

<img src="https://streak-stats.demolab.com?user=kaikea1meida&theme=tokyonight&hide_border=true" alt="GitHub streak statistics">

</div>

---

## `05.` Contact

### email - kaikeaes@gmail.com
### instagram - @kaikea1meida
### discord bacato.
<div align="center">

[![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/kaikea1meida)

</div>

---

<div align="center">

**TY for your time!!!**

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:00599C,100:24292e&height=100&section=footer" width="100%" alt="Footer decoration">

</div>
