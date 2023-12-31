from selene import browser, by, have
import os.path

def test_registration(browser_management):
    browser.open('/automation-practice-form')
    browser.element('#firstName').type('Madina')
    browser.element('#lastName').type('ABDULAEVA')
    browser.element('#userEmail').type('i@mabdulaeva.ru')
    browser.element('#gender-radio-2').double_click()
    browser.element('#userNumber').type('9258880099')

    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__month-select').click().element(by.text('October')).click()
    browser.element('.react-datepicker__year-select').click().element(by.text('1998')).click()
    browser.element('.react-datepicker__day--020').click()

    browser.element('#subjectsInput').set_value('Chemistry').press_enter()
    browser.element('[for=hobbies-checkbox-3]').click()
    browser.element('#uploadPicture').send_keys(os.path.abspath('picture/plumeria.jpg'))
    browser.element('#currentAddress').type('Jerome Hanks Str., h.149, apt.09')

    browser.element('#react-select-3-input').type('Uttar Pradesh').press_enter()
    browser.element('#react-select-4-input').type('Agra').press_enter()
    browser.element('#submit').press_enter()

    browser.element('.modal-header').should(have.text('Thanks for submitting the form'))
    browser.all('tbody tr td:last-child').should(have.exact_texts('Madina ABDULAEVA', 'i@mabdulaeva.ru', 'Female', '9258880099', '20 October,1998', 'Chemistry',
                         'Music', 'plumeria.jpg', 'Jerome Hanks Str., h.149, apt.09', 'Uttar Pradesh Agra'))

    browser.element('#closeLargeModal').press_enter()



