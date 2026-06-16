# Dual Task Temporal Sync Paradigm

A PsychoPy-based cognitive experiment that measures human time perception accuracy under dual-task conditions. Participants estimate elapsed durations while simultaneously reading aloud distractor text, preventing inner verbal counting and isolating the internal clock mechanism.

---

## Overview

This paradigm implements a **temporal reproduction task with a concurrent verbal load**. On each trial, participants observe a blue circle for a target duration (9.5 – 18 seconds) while reading humorous distractor sentences aloud. They then reproduce that duration on a green circle by pressing SPACE to start and stop. The verbal task suppresses counting strategies, revealing the fidelity of the participant's internal clock under cognitive interference.

Results are scored against clinical markers for **dyschronometria** — systematic deviation in time perception associated with ADHD, executive function research, and related conditions.

---

## Task Structure

| Phase | Stimulus | Participant Action |
|---|---|---|
| Encoding | Blue circle + distractor text | Read text aloud; passively experience the interval |
| Reproduction | Green circle + distractor text | Press SPACE to start/stop when the felt interval has elapsed |

**Target durations:** 9.5 s, 12.0 s, 15.5 s, 18.0 s (randomised across 4 trials)

---

## Output Metrics

After all trials, the script prints a full analysis to the console:

- **Per-trial breakdown** — target time, reproduced time, absolute error, and direction (over/under)
- **Mean Absolute Error (MAE)** — average deviation from target in seconds
- **Mean Time Perception Ratio** — `reproduced / target`; values < 1.0 indicate underestimation
- **Standard Deviation** — trial-to-trial consistency of the internal clock

### Classification thresholds

| Metric | Normal range | Flag |
|---|---|---|
| Mean ratio | 0.80 – 1.20 | < 0.80 = temporal shortening; > 1.20 = overestimation |
| Std deviation | ≤ 3.0 s | > 3.0 s = erratic variance |

A **SIGNIFICANT DYSCHRONOMETRIA** profile requires both temporal shortening (ratio < 0.80) and high variance (SD > 3.0 s). Either alone is classified as sub-clinical variance, typical under cognitive load.

---

## Requirements

- Python 3.8+
- [PsychoPy](https://www.psychopy.org/) (`pip install psychopy`)

---

## Usage

```bash
git clone https://github.com/<your-org>/dual-task-temporal-sync-paradigm.git
cd dual-task-temporal-sync-paradigm
python paradigm.py
```

Follow the on-screen instructions:

1. Read the welcome screen and press any key to begin.
2. When the **blue circle** appears, read the text inside it aloud continuously. Do **not** count silently.
3. When the **green circle** appears, press `SPACE` to start your reproduction and `SPACE` again when you feel the same amount of time has passed.
4. Results print to the terminal after all 4 trials.

---

## Design Notes

- **Verbal suppression** is enforced via instruction and the presence of readable text inside the stimulus circle, occupying the phonological loop and blocking subvocal counting.
- **Distractor sentences** are drawn from a pool of 8 humorous passages, shuffled independently for encoding and reproduction phases to avoid repetition within a trial.
- Trial order is fully randomised across participants.
- The paradigm is intentionally lightweight (no data file output) for quick classroom or demonstration use; add a `csv` export to `results` for research data collection.

---
