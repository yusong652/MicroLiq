"""Phase 1: Consolidate to target void ratios.

Compresses specimen from loosest to densest with friction=0,
saving a state for each target void ratio.

Usage in PFC IPython console:
    %run consolidation/consolidate_void.py
"""

from consolidate import ConsolidationServo

import itasca as it


# ── Configuration ─────────────────────────────────────────────

# Edit this list to add/remove target void ratios.
# Will be processed from loosest to densest.
# Dr reference (Toyoura e_min=0.605, e_max=0.977):
#   0.692 -> Dr 76.6%    0.680 -> Dr 79.8%    0.671 -> Dr 82.3%
#   0.661 -> Dr 85.0%    0.655 -> Dr 86.6%    0.650 -> Dr 87.9%
#   0.641 -> Dr 90.3%    0.620 -> Dr 95.9%
TARGET_VOID_RATIOS = [0.692, 0.680, 0.671, 0.661, 0.655, 0.650, 0.641, 0.620]


# ── Main ──────────────────────────────────────────────────────

if __name__ == '__main__':
    # Assumes current loaded state is at or looser than the loosest target
    # (e.g. post_insert or comp_quick_e0.70). Uncomment the restore if you
    # want a deterministic fresh start from comp_quick_e0.71.
    # it.command("model restore 'comp_quick_e0.71'")

    servo = ConsolidationServo()

    def servo_callback():
        servo.cycle()

    for e_tgt in sorted(TARGET_VOID_RATIOS, reverse=True):
        servo.consolidate_to_void_ratio(e_tgt)
        it.command("model save 'comp_e_%.3f'" % e_tgt)
        print("Saved: comp_e_%.3f (e=%.4f)\n" % (e_tgt, servo.void_ratio))
