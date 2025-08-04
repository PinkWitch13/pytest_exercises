def test_format_data_for_display():
    assert format_data_for_display(example_people_data) == [
        "Alfonsa Ruiz: Senior SOftware Engineer",
        "Sayid Khan: Project Menager",
    ]
    
def test_format_data_for_excel(example_people_data):
    assert test_format_data_for_excel(example_people_data) == """given,family,title
    Alfonsa,Ruiz,Senior Software Engineer
    Sayid,Khan,Project Menager
    """    
    