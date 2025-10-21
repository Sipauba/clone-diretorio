import filecmp
from frame_entry_clone import entry_clone
from frame_entry_original import entry_original
from function_copy import function_copy

def function_check_difference():

    from frame_entry_clone import entry_clone
    from frame_entry_original import entry_original

    path_original = entry_original.get()
    path_clone = entry_clone.get()

    iguais = filecmp.dircmp(path_original, path_clone)

    if iguais.left_only or iguais.right_only or iguais.diff_files:
        function_copy(path_original, path_clone)