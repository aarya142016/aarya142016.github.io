# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a GitHub Pages personal website for Aarya Patel, built with Astro and Tailwind CSS. The site showcases Aarya's accomplishments across coding, books, math, music, and art, organized by both topic and school year.

## Tech Stack

- **Astro**: Static site generator for content-focused sites
- **Tailwind CSS**: Utility-first styling with dark mode support
- **Node.js 22+**: Required for the latest Astro

## Development Commands

**IMPORTANT**: This project requires Node.js 22+. Install via nvm:
```bash
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.40.0/install.sh | bash
nvm install 22
nvm use 22
```

**Common tasks:**
```bash
# Install dependencies
npm install

# Start development server
npm run dev
# Site runs at http://localhost:4321

# Build for production
npm run build
# Output is in dist/

# Preview production build
npm run preview
```

## File Structure

```
/
├── src/
│   ├── pages/              # Route pages (.astro files)
│   │   ├── index.astro     # Homepage
│   │   ├── topics/         # Topic pages (coding, books, math, etc.)
│   │   └── years/          # Year summary pages
│   ├── components/         # Reusable Astro components
│   │   ├── Navigation.astro
│   │   ├── Card.astro
│   │   └── BookReview.astro
│   ├── layouts/           # Layout components
│   │   └── Layout.astro    # Base layout with nav/footer
│   └── styles/            # Global styles
│       └── global.css     # Tailwind imports + custom theme
├── public/                # Static assets (served as-is)
│   └── snake/            # Snake game (Python/Pygame)
├── templates/            # Content templates for Aarya to use
│   └── book-review-template.md
├── dist/                 # Build output (deployed to GitHub Pages)
├── astro.config.mjs      # Astro configuration
└── tailwind.config.mjs   # Tailwind configuration
```

## Theme & Styling

**Dark/Light Mode**: Site supports dark/light toggle with localStorage persistence. Default is dark.

**Custom Colors** (defined in `src/styles/global.css`):
- `--color-slate-900`: `#0f172a` (dark background)
- `--color-slate-800`: `#1e293b` (cards/headers)
- `--color-blue-400`: `#60a5fa` (links)

**Component Usage**:
```astro
import Card from '../components/Card.astro';
import BookReview from '../components/BookReview.astro';

<Card title="Title" emoji="🎯">
  <p>Content here</p>
</Card>

<BookReview
  title="Book Title"
  author="Author"
  yearRead={2024}
  rating={5}
  summary="..."
  learned={["item1", "item2"]}
  favoritePart="..."
  recommend="..."
/>
```

## Adding Content

**New Topic Page**: Create `src/pages/topics/new-topic.astro` using existing pages as templates.

**New Year Page**: Create `src/pages/years/grade-X.astro` following the Grade 4 pattern.

**Book Reviews**: Aarya writes reviews using `templates/book-review-template.md`. Currently hard-coded in `src/pages/topics/books.astro` but can be moved to content collections later.

## Snake Game

The Snake game is in `public/snake/` and runs via PyScript:
- `snake.html` - HTML container that loads PyScript
- `snake.py` - Python/Pygame game code
- Access at `/snake/snake.html` on the deployed site

**Key Implementation Detail**: The game loop uses `await asyncio.sleep(1/10)` for ~10 FPS frame control (required by PyScript's async model).

## GitHub Pages Deployment

The `dist/` folder is deployed to GitHub Pages. To deploy:

```bash
npm run build
# Deploy dist/ contents to gh-pages branch
```

Or set up GitHub Actions for automatic deployment on push to main.

## Git Workflow

```bash
git add .
git commit -m "message"
git push origin main
```

Note: This repo deploys to GitHub Pages, so changes appear at the gh-pages URL after push.
