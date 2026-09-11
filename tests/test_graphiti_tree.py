from _tree import load_edges
def test_graphiti_research_reconstructs_three_source_surfaces():
    r={e["relation"] for e in load_edges() if e["from"]=="graphiti-retrieval-relevance"}; assert {"HAS_DISCUSSION_HISTORY","HAS_NOTION_PAGE","HAS_EXECUTABLE_EVIDENCE","HAS_REASONING_LOG"}<=r
