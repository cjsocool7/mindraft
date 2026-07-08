# Mindraft

A desktop mind-mapping application built from scratch with Python and PySide6.

## About
Mindvec is a personal project built for learning purposes. 
The goal is to build a clean, minimal mind-mapping tool 
where you can create nodes, connect them, and organize 
your thoughts visually on an infinite canvas.

## Tech Stack
- Python
- PySide6 (Qt for Python)

## Project Structure
mindvec/
├── models/         ← data layer (nodes, edges, graph)
├── views/          ← GUI layer (canvas, node items, edge items)
├── controllers/    ← connects models and views
└── utils/          ← constants and shared helpers

## Phase 1 — MVP (In Progress)
- [x] Create nodes
- [ ] Connect nodes with edges
- [ ] Drag nodes on canvas
- [ ] Delete nodes
- [ ] Edit node labels

## Phase 2 — Planned
- [ ] Save and load mind maps
- [ ] Multiple mind maps
- [ ] Home screen
