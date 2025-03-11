def generate_insights(analysis_results):
    insights = []
    # Analyze the detected events and generate insights
    for result in analysis_results:
        frame_idx = result["frame_idx"]
        timestamp = result["timestamp"]
        objects = result["objects"]
        
        # Example insight: Detect goals
        for obj in objects:
            if obj['name'] == 'ball' and obj['confidence'] > 0.5:
                # Check if the ball is in the goal area
                if obj['xmin'] < goal_area_xmax and obj['xmax'] > goal_area_xmin and obj['ymin'] < goal_area_ymax and obj['ymax'] > goal_area_ymin:
                    insights.append(f"Goal detected at {timestamp:.2f} seconds (frame {frame_idx})")
                    
        # Add more detailed analysis for other events (tackles, passes, etc.)
    
    return insights

# Define the goal area (example values, should be adjusted based on actual video dimensions)
goal_area_xmin = 0
goal_area_xmax = 100
goal_area_ymin = 400
goal_area_ymax = 600