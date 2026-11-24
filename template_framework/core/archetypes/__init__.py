from .grid_cards import generate_grid_cards_html
from .leaderboard import generate_leaderboard_html
from .process_flow import generate_process_flow_html
from .workspace_prd import generate_workspace_prd_html
from .app_satellites import generate_app_satellites_html
from .poster_outro import generate_poster_outro_html

ARCHETYPE_GENERATORS = {
    "grid_cards": generate_grid_cards_html,
    "card_matrix": generate_grid_cards_html,
    "leaderboard": generate_leaderboard_html,
    "process_flow": generate_process_flow_html,
    "pipeline_comparison": generate_process_flow_html,
    "workspace_prd": generate_workspace_prd_html,
    "workflow_prd": generate_workspace_prd_html,
    "app_satellites": generate_app_satellites_html,
    "product_showcase": generate_app_satellites_html,
    "poster_outro": generate_poster_outro_html,
    "checklist_cta_outro": generate_poster_outro_html
}

def get_archetype_generator(type_name):
    return ARCHETYPE_GENERATORS.get(type_name)
