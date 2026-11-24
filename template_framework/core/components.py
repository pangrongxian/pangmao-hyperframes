"""
Reusable UI Components for Video Archetypes:
- Header Navigation (Chapter Number + Title)
- Brand Arch Canopy
- Presenter Avatar HUD
- Subtitle Capsule
- Hand Pointer SVG
"""

def render_header(chapter_num_str, chapter_title_str, brand_name="胖猫"):
    return f"""
    <!-- Top Navigation Header -->
    <div class="header-nav">
      <span class="nav-num">{chapter_num_str}</span>
      <span class="nav-title">{chapter_title_str}</span>
    </div>

    <!-- Top Right Brand Arch -->
    <div class="header-brand">
      <div class="brand-arch"></div>
      <div class="brand-title">{brand_name}</div>
    </div>
"""

def render_presenter_hud(avatar_src="../assets/avatar.jpg", hud_id="s-avatar"):
    return f"""
    <!-- Presenter Avatar HUD -->
    <div class="avatar-hud" id="{hud_id}">
      <img src="{avatar_src}" alt="Presenter Avatar" />
    </div>
"""

def render_subtitle_hud(initial_text="", sub_id="s-sub"):
    return f"""
    <!-- Elevated Subtitle Capsule -->
    <div class="subtitle-hud">
      <div class="subtitle-capsule">
        <div class="subtitle-text" id="{sub_id}">{initial_text}</div>
      </div>
    </div>
"""

def render_pointer(pointer_id="s-pointer"):
    return f"""
    <!-- Interactive Hand Pointer Cursor -->
    <div class="hand-pointer" id="{pointer_id}">
      <svg width="48" height="48" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
        <path d="M10 2L10 12M10 12L7.5 9.5M10 12L12.5 9.5" stroke="#1E2024" stroke-width="2" stroke-linecap="round"/>
        <path d="M8 12V6.5C8 5.67157 8.67157 5 9.5 5C10.3284 5 11 5.67157 11 6.5V11M11 9C11 8.17157 11.6716 7.5 12.5 7.5C13.3284 7.5 14 8.17157 14 9V11.5M14 10.5C14 9.67157 14.6716 9 15.5 9C16.3284 9 17 9.67157 17 10.5V14C17 17.3137 14.3137 20 11 20C8.5 20 6.5 18.5 5.5 16.5L4 13L5.5 12.5L7.5 14.5" fill="#FFFFFF" stroke="#1E2024" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
      </svg>
    </div>
"""
