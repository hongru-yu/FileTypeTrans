"""
进度显示模块的单元测试
"""
from src.ui.progress import ProgressTracker


class TestProgressTracker:
    """测试进度跟踪器"""

    def test_initialization(self):
        """测试初始化"""
        tracker = ProgressTracker(total=100)

        assert tracker.total == 100
        assert tracker.processed == 0
        assert tracker.success == 0
        assert tracker.failed == 0
        assert tracker.skipped == 0

    def test_increment_processed(self):
        """测试增加已处理数量"""
        tracker = ProgressTracker(total=10)

        tracker.increment_processed()
        assert tracker.processed == 1

        tracker.increment_processed(5)
        assert tracker.processed == 6

    def test_increment_success(self):
        """测试增加成功数量"""
        tracker = ProgressTracker(total=10)

        tracker.increment_success()
        assert tracker.success == 1

        tracker.increment_success(3)
        assert tracker.success == 4

    def test_increment_failed(self):
        """测试增加失败数量"""
        tracker = ProgressTracker(total=10)

        tracker.increment_failed()
        assert tracker.failed == 1

        tracker.increment_failed(2)
        assert tracker.failed == 3

    def test_increment_skipped(self):
        """测试增加跳过数量"""
        tracker = ProgressTracker(total=10)

        tracker.increment_skipped()
        assert tracker.skipped == 1

        tracker.increment_skipped(4)
        assert tracker.skipped == 5

    def test_get_percentage(self):
        """测试获取进度百分比"""
        tracker = ProgressTracker(total=100)

        assert tracker.get_percentage() == 0.0

        tracker.increment_processed(50)
        assert tracker.get_percentage() == 50.0

        tracker.increment_processed(50)
        assert tracker.get_percentage() == 100.0

    def test_get_percentage_zero_total(self):
        """测试总数为零时的百分比"""
        tracker = ProgressTracker(total=0)

        assert tracker.get_percentage() == 0.0

    def test_is_complete(self):
        """测试是否完成"""
        tracker = ProgressTracker(total=10)

        assert not tracker.is_complete()

        tracker.increment_processed(10)
        assert tracker.is_complete()

    def test_get_summary(self):
        """测试获取摘要"""
        tracker = ProgressTracker(total=10)
        tracker.increment_success(5)
        tracker.increment_failed(2)
        tracker.increment_skipped(3)

        summary = tracker.get_summary()

        assert "总数" in summary
        assert "10" in summary
        assert "成功: 5" in summary
        assert "失败: 2" in summary
        assert "跳过: 3" in summary
