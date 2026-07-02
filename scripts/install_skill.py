"""
install_skill.py — 将 summary-work skill 安装到 Codex
"""
import os
import shutil
from pathlib import Path

SRC_BASE = Path(r"D:\project mangers\Summary Skill")
CODEx_SKILLS = Path.home() / ".codex" / "skills"
DEST = CODEx_SKILLS / "summary-work"

def install():
    DEST.mkdir(parents=True, exist_ok=True)
    
    # Copy SKILL.md
    src_skill = SRC_BASE / "SKILL.md"
    dst_skill = DEST / "SKILL.md"
    if src_skill.exists():
        shutil.copy2(src_skill, dst_skill)
        print(f"[OK] SKILL.md -> {dst_skill}")
    else:
        print("[WARN] SKILL.md not found at source")
    
    # Copy references
    refs_src = SRC_BASE / "references"
    refs_dst = DEST / "references"
    if refs_src.exists():
        if refs_dst.exists():
            shutil.rmtree(refs_dst)
        shutil.copytree(refs_src, refs_dst)
        print(f"[OK] references/ -> {refs_dst}/")
    
    # Copy scripts
    scripts_src = SRC_BASE / "scripts"
    scripts_dst = DEST / "scripts"
    if scripts_src.exists():
        if scripts_dst.exists():
            shutil.rmtree(scripts_dst)
        shutil.copytree(scripts_src, scripts_dst)
        print(f"[OK] scripts/ -> {scripts_dst}/")
    
    print(f"\n[Done] summary-work skill installed at: {DEST}")

if __name__ == "__main__":
    install()