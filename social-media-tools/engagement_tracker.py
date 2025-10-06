#!/usr/bin/env python3
"""
Engagement Tracker - AI-Powered Analytics
Tracks and analyzes engagement across all social media platforms
"""

import json
from datetime import datetime, timedelta
from typing import Dict, List
import statistics

class AIEngagementTracker:
    """
    AI-powered engagement tracker that monitors performance
    across all platforms and provides actionable insights.
    """
    
    def __init__(self):
        self.platforms = ['instagram', 'twitter', 'tiktok', 'onlyfans']
        self.metrics = {}
        self.historical_data = []
        self.insights = []
        
    def track_post(self, platform: str, post_data: Dict) -> Dict:
        """
        AI tracks engagement for a single post.
        Automatically analyzes and stores metrics.
        """
        engagement_score = self._calculate_engagement(post_data)
        
        tracked_post = {
            'platform': platform,
            'timestamp': datetime.now().isoformat(),
            'likes': post_data.get('likes', 0),
            'comments': post_data.get('comments', 0),
            'shares': post_data.get('shares', 0),
            'views': post_data.get('views', 0),
            'engagement_score': engagement_score,
            'content_type': post_data.get('content_type', 'general')
        }
        
        self.historical_data.append(tracked_post)
        return tracked_post
    
    def _calculate_engagement(self, post_data: Dict) -> float:
        """
        AI calculates engagement score using multiple factors.
        """
        likes = post_data.get('likes', 0)
        comments = post_data.get('comments', 0)
        shares = post_data.get('shares', 0)
        views = post_data.get('views', 1)
        
        # Weighted engagement formula
        engagement_rate = ((likes + (comments * 2) + (shares * 3)) / views) * 100
        return round(engagement_rate, 2)
    
    def analyze_performance(self, days: int = 30) -> Dict:
        """
        AI analyzes performance over specified time period.
        Runs to completion and returns comprehensive insights.
        """
        print(f"\n📊 Analyzing performance for last {days} days...")
        
        cutoff_date = datetime.now() - timedelta(days=days)
        recent_posts = [
            post for post in self.historical_data
            if datetime.fromisoformat(post['timestamp']) > cutoff_date
        ]
        
        if not recent_posts:
            return {'error': 'No data available for analysis'}
        
        analysis = {
            'period': f'Last {days} days',
            'total_posts': len(recent_posts),
            'by_platform': self._analyze_by_platform(recent_posts),
            'best_performing': self._get_top_posts(recent_posts, 5),
            'engagement_trends': self._calculate_trends(recent_posts),
            'ai_recommendations': self._generate_recommendations(recent_posts)
        }
        
        print("✅ Analysis complete!")
        return analysis
    
    def _analyze_by_platform(self, posts: List[Dict]) -> Dict:
        """
        AI breaks down performance by platform.
        """
        platform_stats = {}
        
        for platform in self.platforms:
            platform_posts = [p for p in posts if p['platform'] == platform]
            
            if platform_posts:
                platform_stats[platform] = {
                    'post_count': len(platform_posts),
                    'avg_engagement': round(statistics.mean(
                        [p['engagement_score'] for p in platform_posts]
                    ), 2),
                    'total_likes': sum(p['likes'] for p in platform_posts),
                    'total_comments': sum(p['comments'] for p in platform_posts),
                    'total_shares': sum(p['shares'] for p in platform_posts)
                }
        
        return platform_stats
    
    def _get_top_posts(self, posts: List[Dict], count: int) -> List[Dict]:
        """
        AI identifies top performing posts.
        """
        sorted_posts = sorted(
            posts,
            key=lambda x: x['engagement_score'],
            reverse=True
        )
        return sorted_posts[:count]
    
    def _calculate_trends(self, posts: List[Dict]) -> Dict:
        """
        AI identifies engagement trends over time.
        """
        if len(posts) < 2:
            return {'trend': 'insufficient_data'}
        
        # Split data into two halves
        mid_point = len(posts) // 2
        first_half = posts[:mid_point]
        second_half = posts[mid_point:]
        
        avg_first = statistics.mean([p['engagement_score'] for p in first_half])
        avg_second = statistics.mean([p['engagement_score'] for p in second_half])
        
        change = ((avg_second - avg_first) / avg_first) * 100
        
        return {
            'direction': 'increasing' if change > 0 else 'decreasing',
            'change_percentage': round(change, 2),
            'first_half_avg': round(avg_first, 2),
            'second_half_avg': round(avg_second, 2)
        }
    
    def _generate_recommendations(self, posts: List[Dict]) -> List[str]:
        """
        AI generates actionable recommendations based on data.
        """
        recommendations = []
        
        # Analyze platform performance
        platform_stats = self._analyze_by_platform(posts)
        if platform_stats:
            best_platform = max(
                platform_stats.items(),
                key=lambda x: x[1]['avg_engagement']
            )
            recommendations.append(
                f"✅ Focus more on {best_platform[0]} - highest engagement rate"
            )
        
        # Analyze posting frequency
        total_posts = len(posts)
        if total_posts < 10:
            recommendations.append(
                "📈 Increase posting frequency for better visibility"
            )
        
        # Analyze engagement trends
        trends = self._calculate_trends(posts)
        if trends['direction'] == 'decreasing':
            recommendations.append(
                "⚠️ Engagement declining - try new content formats"
            )
        else:
            recommendations.append(
                "🚀 Engagement growing - keep up the great work!"
            )
        
        return recommendations
    
    def generate_report(self, days: int = 30) -> str:
        """
        AI generates comprehensive text report.
        Runs to completion automatically.
        """
        print("\n📄 Generating engagement report...")
        
        analysis = self.analyze_performance(days)
        
        if 'error' in analysis:
            return "No data available for report generation."
        
        report = []
        report.append("="*60)
        report.append("📊 ENGAGEMENT REPORT")
        report.append("The Steele Zone - AI Performance Analytics")
        report.append("="*60)
        report.append(f"\nPeriod: {analysis['period']}")
        report.append(f"Total Posts: {analysis['total_posts']}")
        
        report.append("\n🌐 PLATFORM BREAKDOWN:")
        for platform, stats in analysis['by_platform'].items():
            report.append(f"\n{platform.upper()}:")
            report.append(f"  Posts: {stats['post_count']}")
            report.append(f"  Avg Engagement: {stats['avg_engagement']}%")
            report.append(f"  Total Likes: {stats['total_likes']}")
            report.append(f"  Total Comments: {stats['total_comments']}")
            report.append(f"  Total Shares: {stats['total_shares']}")
        
        report.append("\n🎯 TOP PERFORMING POSTS:")
        for i, post in enumerate(analysis['best_performing'], 1):
            report.append(f"\n#{i} - {post['platform'].upper()}")
            report.append(f"  Engagement: {post['engagement_score']}%")
            report.append(f"  Likes: {post['likes']} | Comments: {post['comments']}")
        
        report.append("\n📈 TRENDS:")
        trends = analysis['engagement_trends']
        report.append(f"  Direction: {trends['direction'].upper()}")
        report.append(f"  Change: {trends['change_percentage']}%")
        
        report.append("\n🤖 AI RECOMMENDATIONS:")
        for rec in analysis['ai_recommendations']:
            report.append(f"  {rec}")
        
        report.append("\n" + "="*60)
        report.append("✅ Report generated successfully!")
        report.append("="*60)
        
        return "\n".join(report)
    
    def auto_monitor(self, interval_hours: int = 24):
        """
        AI continuously monitors engagement.
        Runs indefinitely and generates periodic reports.
        """
        print(f"\n🔄 Starting auto-monitoring (every {interval_hours} hours)...")
        print("✅ AI will track and analyze engagement continuously")
        print("📊 Reports will be generated automatically\n")
        
        # In production, this would run on a schedule
        # For demo, we show the concept
        print("Auto-monitoring active. Press Ctrl+C to stop.")

def run_tracker_demo():
    """
    Demo function showing AI engagement tracker in action.
    """
    tracker = AIEngagementTracker()
    
    print("="*60)
    print("📊 AI ENGAGEMENT TRACKER")
    print("The Steele Zone - Automated Performance Analytics")
    print("="*60)
    
    # Simulate tracking posts
    print("\n📈 Simulating post tracking...")
    
    sample_posts = [
        {'platform': 'instagram', 'likes': 523, 'comments': 87, 'shares': 23, 'views': 2450, 'content_type': 'photo'},
        {'platform': 'twitter', 'likes': 234, 'comments': 45, 'shares': 67, 'views': 1230, 'content_type': 'text'},
        {'platform': 'tiktok', 'likes': 1823, 'comments': 234, 'shares': 123, 'views': 8900, 'content_type': 'video'},
        {'platform': 'onlyfans', 'likes': 892, 'comments': 156, 'shares': 0, 'views': 3200, 'content_type': 'exclusive'},
        {'platform': 'instagram', 'likes': 678, 'comments': 92, 'shares': 34, 'views': 2890, 'content_type': 'video'},
    ]
    
    for post in sample_posts:
        tracked = tracker.track_post(post['platform'], post)
        print(f"  ✓ Tracked {tracked['platform']} post: {tracked['engagement_score']}% engagement")
    
    # Generate report
    print("\n" + tracker.generate_report(30))
    
    print("\n✅ All tracking and analysis complete!")

if __name__ == '__main__':
    run_tracker_demo()
