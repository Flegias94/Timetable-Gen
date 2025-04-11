from typing import List, Tuple
from itertools import combinations
from collections import defaultdict
from models.entities import StudentGroup


def get_mergeable_subgroups(groups: List[StudentGroup], max_size: int):
    """
    Returns combinations of subgroups that can be merged together,
    up to the max allowed size (e.g., room capacity).
    """
    from itertools import combinations

    merge_candidates = []

    # Group by parent
    from collections import defaultdict

    parent_map = defaultdict(list)
    for g in groups:
        parent_map[g.parent_id].append(g)

    for parent, subs in parent_map.items():
        # Try all combinations of 2, 3, ... up to all subs
        for r in range(1, len(subs) + 1):
            for combo in combinations(subs, r):
                total = sum(g.size for g in combo)
                if total <= max_size:
                    merge_candidates.append(combo)

    return merge_candidates
