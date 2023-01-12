def get_corrected_names(names: list) -> list:
    corrected_nicknames = []
    for nickname in names:
        corrected_nicknames.append(f"@{nickname}")
    return corrected_nicknames
