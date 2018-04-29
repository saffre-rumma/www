from atelier.invlib import setup_from_tasks
ns = setup_from_tasks(globals())

cfg = dict()
# cfg.update(tolerate_sphinx_warnings=True)
# cfg.update(blog_root='/home/luc/work/blog/')
# cfg.update(languages=['en'])
cfg.update(revision_control_system='git')
cfg.update(doc_trees=[
    ("atelier.invlib.utils.NikolaTree", ".")])
# cfg.update(
#     docs_rsync_dest='luc@167.114.252.122:~/public_html/{prj}')
ns.configure(cfg)

