DEFAULT_STATEMENT = -2
SWITCH_MISSING_DEFAULT_NODE_ADDR = 0xFFFF_FFFE


def is_alignment_mask(n):
    return n in {0xFFFFFFFFFFFFFFE0, 0xFFFFFFFFFFFFFFF0, 0xFFFFFFF0, 0xFFFFFFFC}
