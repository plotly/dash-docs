def test_snap100_component_sub_pages(component_map, dash_doc):
    for _, grouper in component_map:
        for resources in grouper:
            href = "/".join(resources)
            dash_doc.visit_and_snapshot(
                href, hook_id="wait-for-page-/{}".format(href)
            )
