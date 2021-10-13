from app.page.securities import SecurityDetail

title = 'Visualize & Transform'


def is_valid(data):
    return True


def render(data, index):
    data = SecurityDetail(data).render()
    return data
