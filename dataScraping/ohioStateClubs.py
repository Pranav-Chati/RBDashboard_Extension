#before any clubs:
#https://activities.osu.edu/involvement/student_organizations/find_a_student_org

#after all clubs loaded in:
#https://activities.osu.edu/involvement/student_organizations/find_a_student_org?v=card&c=Columbus

#second page:
#https://activities.osu.edu/involvement/student_organizations/find_a_student_org?page=1&v=card&c=Columbus

#notice the page=1 in the middle, page = 0 loads very slowly

#URL: https://activities.osu.edu/involvement/student_organizations/find_a_student_org?page=0&v=card&c=Columbus

### Make sure packages are installed:
# pip install BeautifulSoup4
# pip install requests
# pip install pandas

# import libraries
from bs4 import BeautifulSoup
import requests
import pandas as pd

# declare variables
clubCards = []
clubNames = []
clubCategories = []
clubDescriptions = []

### TODO: Make these not variable but rather defined. Is there a way to know that 106 is the max number of elements
## the end is 106, since range is not inclusive, so 105 is the last page
for pageNumber in range(0, 106):
    print(pageNumber)
    # call html
    url = 'https://activities.osu.edu/involvement/student_organizations/find_a_student_org?page=' + str(pageNumber) + '&v=card&c=Columbus'
    req = requests.get(url)

    context = req.text
    soup = BeautifulSoup(context, "html.parser")

    # extract out useful information and save it into a structured format
    for card in soup.find("div", class_= "o-row__col o-row__col--4of12@md").parent.children:
        # the children include a new line character, so must check to get rid of it
        if card != '\n':
            # each card is the singular element
            clubCards.append([card])

            clubName = ' '
            if card.find("h2") is not None: clubName = card.find("h2").contents[0].strip()
            clubNames.append(clubName)

            clubCategory = ' '
            if card.find("p") is not None: clubCategory = card.find("p").contents[0].strip()
            clubCategories.append(clubCategory)

            clubDescription = ' '
            if card.find("div", class_="c-card__description") is not None: clubDescription = card.find("div", class_="c-card__description").contents[0].strip()

            clubDescriptions.append(clubDescription)

#save data into an output
output = pd.DataFrame({
    'Club Name': clubNames,
    'Categories': clubCategories,
    'Description': clubDescriptions
})

print(output)