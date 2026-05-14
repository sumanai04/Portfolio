# Portfolio Improvement Plan

## Done

- [x] **Fix typos** — `classifcating`, `capabilites`, `survivality`, `analyzed` all fixed
- [x] **Expand hero bio** — Replaced vague one-liner with 3-line blurb (CS grad, ML/CV focus, end-to-end pipeline to deployment)
- [x] **Add metrics to project descriptions** — Pulled real details from GitHub READMEs: DR Segmentation (hybrid loss, A100 GPU, AUPR/Dice/IoU), Hand Gesture (MediaPipe + TensorFlow, Creative Senz3D dataset with ~1,060 images, 11 gestures)
- [x] **Differentiate project cards** — Top 4 projects get coral left accent border via `.project-card.featured`
- [x] **Hobbies narrative hook** — Changed from "Little things I do here and there" to "Building things doesn't stop at the screen"
- [x] **Added missing project** — WebAgenticStarterKit (dual-agent LiteLLM/DeepSeek/Ollama boilerplate) was in GitHub but not the portfolio
- [x] **Added project visual** — DR Segmentation card now has a thumbnail (qualitative masks comparison from the repo)
- [x] **Switched CV to LaTeX version** — Download link now points to `Fathi_CV_AI_Latex.pdf`
- [x] **Performance fixes** — Removed backdrop-filter blur (GPU killer), resized background from 2.9MB to 237KB, optimized all thumbnails

## Still to do

### 1. Add more project thumbnails
- DR Segmentation: done
- Hand Gesture: could use a GIF or architecture diagram from the repo
- Receipt-Inator: needs a UI screenshot
- WebAgenticStarterKit: architecture flowchart is in the README — could embed it
- Others: screenshots would help but only if they exist

### 2. Merge or expand Data Viz section
- One Power BI embed under "Data Visualizations" (plural) reads as incomplete
- Option A: merge it into Projects
- Option B: add more dashboards

### 3. Add project detail modals
- Clicking a project card goes straight to GitHub. A detail modal with full README excerpt, screenshots, and tech breakdown would be more compelling. GitHub link can still be the final CTA.

### 4. Update CV content
- `Fathi_CV_AI_Latex.pdf` needs the `.tex` source file to edit
- Once provided, can update with latest projects, skills, and roles

### 5. Reorder projects
- Currently: DR Segmentation, Hand Gesture, StuntingApp, Receipt-Inator, WebAgenticStarterKit, MobAppOTP, Boolean Retrieval, Genetic Algorithm, Disease Classification, Covid Dashboard, Redis Quiz
- Better order: featured first (DR Segmentation, Hand Gesture, Receipt-Inator, WebAgenticStarterKit), then the rest by category

### 6. Consider removing or demoting weaker projects
- StuntingApp (HTML + JS blog) sits next to WebAgenticStarterKit (Next.js + FastAPI + PostgreSQL + LiteLLM) — the contrast makes the portfolio look uneven
- Option: hide weaker projects behind a "show more" toggle, or remove entirely

### 7. Deduplicate CV files
- `Fathi_CV_AI.pdf` (61.9 KB) and `Fathi_CV_AI_Latex.pdf` — only the LaTeX one is linked. The old one can be removed to avoid confusion.

### 8. Add MusicClassifyDL
- New repo found but README is empty. Worth adding only if there's content to describe.
