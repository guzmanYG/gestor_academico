from .structures import BST

def build_bst_from_queryset(queryset):
    bst = BST()
    for s in queryset:
        bst.insert(s.matricula, s)
    return bst
