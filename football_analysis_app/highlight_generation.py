from moviepy.editor import VideoFileClip, concatenate_videoclips, TextClip, CompositeVideoClip

# Define the goal area (example values, should be adjusted based on actual video dimensions)
goal_area_xmin = 0
goal_area_xmax = 100
goal_area_ymin = 400
goal_area_ymax = 600

def generate_highlights(analysis_results):
    highlight_clips = []
    
    for result in analysis_results:
        frame_idx = result["frame_idx"]
        timestamp = result["timestamp"]
        objects = result["objects"]
        
        # Example: Generate a highlight clip for a detected goal
        for obj in objects:
            if obj['name'] == 'ball' and obj['confidence'] > 0.5:
                if obj['xmin'] < goal_area_xmax and obj['xmax'] > goal_area_xmin and obj['ymin'] < goal_area_ymax and obj['ymax'] > goal_area_ymin:
                    clip = VideoFileClip("path_to_your_video.mp4").subclip(max(0, timestamp-5), min(timestamp+5, VideoFileClip("path_to_your_video.mp4").duration))
                    txt_clip = TextClip("Goal!", fontsize=70, color='red').set_position('center').set_duration(10)
                    video = CompositeVideoClip([clip, txt_clip])
                    highlight_clips.append(video)
    
    # Concatenate all highlight clips into one video
    final_highlight_video = concatenate_videoclips(highlight_clips)
    final_highlight_video.write_videofile("highlights.mp4", codec="libx264")
    
    return "highlights.mp4"