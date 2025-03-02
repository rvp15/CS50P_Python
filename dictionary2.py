#creating a report for spacecraft:
def main():
    spacecraft={
        "name":"Voyager1",
        "distace":"125"
    }
    ##################MODIFY DITIONARY###########
    spacecraft["year"] =1965   # assign
    spacecraft.update({"country":"USA"})

    ###########################################
    print(create_report(spacecraft))

def create_report(spacecraft):
    return f"""
    ===========Report==========

    Name: {spacecraft["name"]}
    Distance: {spacecraft["distace"]} AU
    Year: {spacecraft["year"]}

    ####another way to access#####

    Country: {spacecraft.get("country")}
    ===========================
    """


main()


