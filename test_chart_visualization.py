# test_chart_visualization.py
# Test script to verify chart visualization in both console and GUI modes

from utils.statistics import StatisticsTracker

def test_ascii_chart():
    """Test ASCII chart generation."""
    print("\n" + "=" * 70)
    print("🧪 TESTING ASCII CHART VISUALIZATION")
    print("=" * 70 + "\n")
    
    # Create a tracker
    tracker = StatisticsTracker()
    
    # Simulate multiple analyses
    test_data = [
        ('High', 'Suspicious email with phishing keywords'),
        ('High', 'Insecure HTTP URL with IP address'),
        ('Medium', 'Email with some concerning language'),
        ('Medium', 'URL with excessive hyphens'),
        ('Medium', 'Email with @ symbol spoofing'),
        ('Low', 'Safe email address format'),
        ('Low', 'Legitimate HTTPS URL'),
        ('High', 'Multiple phishing indicators found'),
    ]
    
    # Add analyses
    for risk_level, description in test_data:
        tracker.add_analysis(risk_level)
        print(f"✓ Added: {risk_level} Risk - {description}")
    
    # Display ASCII chart
    chart = tracker.generate_ascii_chart()
    print(chart)
    
    # Display statistics
    stats = tracker.get_stats()
    print(f"\n📊 Statistics Summary:")
    print(f"   Total Analyses: {stats['total']}")
    print(f"   High Risk: {stats['high']}")
    print(f"   Medium Risk: {stats['medium']}")
    print(f"   Low Risk: {stats['low']}")
    print()
    
    return tracker

def test_matplotlib_chart(tracker):
    """Test matplotlib chart generation."""
    print("\n" + "=" * 70)
    print("🧪 TESTING MATPLOTLIB CHART VISUALIZATION")
    print("=" * 70 + "\n")
    
    try:
        import matplotlib.pyplot as plt
        
        # Generate chart
        fig = tracker.generate_matplotlib_chart("Test Phishing Detection Statistics")
        
        print("✅ Matplotlib chart generated successfully!")
        print("   Chart title: 'Test Phishing Detection Statistics'")
        print("   Figure size: 10x6 inches")
        print("   Colors: Red (High), Orange (Medium), Green (Low)")
        print("\n💡 To view the chart, uncomment 'plt.show()' in the test script")
        print("   or run in an interactive environment.\n")
        
        # Uncomment to display the chart
        # plt.show()
        
        # Save chart to file for verification
        chart_path = "output/test_chart.png"
        fig.savefig(chart_path, facecolor='#0a0e27')
        print(f"✅ Chart saved to: {chart_path}")
        plt.close(fig)
        
    except ImportError:
        print("⚠️  matplotlib not installed. Install with: pip install matplotlib")
        print("   Chart generation skipped for this test.")

if __name__ == "__main__":
    print("\n" + "╔" + "=" * 68 + "╗")
    print("║" + " " * 68 + "║")
    print("║" + "   🔒 CHART VISUALIZATION TEST".ljust(69) + "║")
    print("║" + " " * 68 + "║")
    print("╚" + "=" * 68 + "╝\n")
    
    # Test ASCII chart
    tracker = test_ascii_chart()
    
    # Test Matplotlib chart
    test_matplotlib_chart(tracker)
    
    print("\n" + "=" * 70)
    print("✅ ALL CHART VISUALIZATION TESTS COMPLETED")
    print("=" * 70 + "\n")
