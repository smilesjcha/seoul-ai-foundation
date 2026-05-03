"""Build seoul-ai-foundation-workshop.pptx from slides_data.SLIDES."""

import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

from pptx import Presentation

import theme as T
import layouts as L
from slides_data import SLIDES


TYPE_TO_FN = {
    "cover": L.make_cover,
    "section_divider": L.make_section_divider,
    "concept": L.make_concept,
    "process": L.make_process,
    "two_column": L.make_two_column,
    "document": L.make_document,
    "code_demo": L.make_code_demo,
    "review": L.make_review,
    "wrap_up": L.make_wrap_up,
    "one_liner": L.make_one_liner,
    "schedule": L.make_schedule,
    "sequence": L.make_sequence_diagram,
    "erd": L.make_erd,
    "card_grid": L.make_card_grid,
    "badge_row": L.make_badge_row,
    "comparison": L.make_comparison,
    "api_table": L.make_api_table,
    "cycle": L.make_cycle,
    "tree": L.make_tree,
}


def build():
    prs = Presentation()
    prs.slide_width = T.SLIDE_W
    prs.slide_height = T.SLIDE_H

    for data in SLIDES:
        kind = data.get("type")
        fn = TYPE_TO_FN.get(kind)
        if fn is None:
            raise ValueError(
                f"Unknown slide type {kind!r} for slide {data.get('no')}"
            )
        fn(prs, data)

    out_dir = os.path.join(HERE, "..", "..", "output")
    out_dir = os.path.abspath(out_dir)
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "seoul-ai-foundation-workshop.pptx")
    prs.save(out_path)
    print(f"Saved: {out_path}")
    print(f"Slides: {len(prs.slides)}")
    return out_path


if __name__ == "__main__":
    build()
