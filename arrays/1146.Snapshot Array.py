# https://leetcode.com/problems/snapshot-array/description/

# 問題敘述
# 實現一個「快照陣列」，它有三個功能：
# 初始化：建立一個長度為 length 的陣列，所有元素初始值為 0。
# 設定值：set(index, val) 把第 index 個位置的值改為 val。
# 拍快照：snap() 記錄目前整個陣列的狀態，並回傳這次快照的編號（從 0 開始依次遞增）。
# 讀取快照：get(index, snap_id) 取出當時第 snap_id 次快照時，第 index 個位置的值。

class SnapshotArray:
    def __init__(self, length: int):
        # 当前的快照编号，从 0 开始
        self.curr_snap = 0
        # history[i] 是一个有序列表，存储“(snap_id, val)”对，
        # 表示在第 snap_id 次快照时，位置 i 的值变为了 val
        # 初始化时，所有位置在 snap 0 的值都是 0
        self.history: List[List[Tuple[int,int]]] = [
            [(0, 0)] for _ in range(length)
        ]

    def set(self, index: int, val: int) -> None:
        recs = self.history[index]
        # 如果最后一条记录正好是当前快照 self.curr_snap，
        # 就直接覆盖它的 val，否则在末尾追加一条新记录
        if recs[-1][0] == self.curr_snap:
            recs[-1] = (self.curr_snap, val)
        else:
            recs.append((self.curr_snap, val))

    def snap(self) -> int:
        # 返回当前快照号，然后自增，为下一次 snap 做准备
        snap_id = self.curr_snap
        self.curr_snap += 1
        return snap_id

    def get(self, index: int, snap_id: int) -> int:
        recs = self.history[index]
        # 在 recs 这个有序的 (snap_id, val) 列表里，
        # 找到“第一个大于 (snap_id, +∞) 的位置” —— bisect_right
        # 减 1 就定位到“最后一个 ≤ snap_id 的记录”
        i = bisect_right(recs, (snap_id, float('inf'))) - 1
        return recs[i][1]