"""@file
@brief Fill a new blog database with example data for the screenshots.

The data is built through the use cases of the application, not through the
browser. Only invented example people and texts are used.
"""

from blog.application.dto import PostContent, Registration
from blog.presentation.app import create_app
from blog.presentation.services import current_use_cases

EXAMPLE_PASSWORD = "example-password-1"  # noqa: S105  (example data, not a secret)
"""@brief Password of every example user."""

ADMIN = Registration(
    email="jane@example.com", password=EXAMPLE_PASSWORD, name="Jane Doe"
)
"""@brief The first registered user, who is the admin."""

MEMBERS = (
    Registration(email="john@example.com", password=EXAMPLE_PASSWORD, name="John Doe"),
    Registration(email="mary@example.com", password=EXAMPLE_PASSWORD, name="Mary Roe"),
)
"""@brief Users who may comment but not manage posts."""

POSTS = (
    PostContent(
        title="The Life of Cactus",
        subtitle="Who knew that cacti lived such interesting lives.",
        img_url="/static/assets/img/post-bg.jpg",
        body=(
            "<p>Cacti store water in their stems, so they can wait months for rain.</p>"
            "<p>Their spines are leaves that learned to save water "
            "and keep animals away.</p>"
        ),
    ),
    PostContent(
        title="Why I like Flask",
        subtitle="A small framework with room to grow.",
        img_url="/static/assets/img/home-bg.jpg",
        body="<p>A route is a function, and a template turns data into a page.</p>",
    ),
)
"""@brief Posts written by the admin."""

COMMENTS = (
    (0, "<p>I never knew that cacti can wait months for rain.</p>"),
    (1, "<p>Great post! Now I want to buy a cactus.</p>"),
    (0, "<p>The part about the spines was my favourite.</p>"),
)
"""@brief Pairs of (index into MEMBERS, comment text) on the first post."""


def seed() -> None:
    """@brief Create the users, posts and comments of the screenshots."""
    app = create_app()
    with app.app_context():
        use_cases = current_use_cases()
        admin = use_cases.register_user.execute(ADMIN)
        members = [use_cases.register_user.execute(member) for member in MEMBERS]
        posts = [use_cases.create_post.execute(post, admin) for post in POSTS]
        first_post_id = posts[0].id
        if first_post_id is None:
            raise RuntimeError("The first post was not stored.")
        for member_index, text in COMMENTS:
            use_cases.add_comment.execute(text, members[member_index], first_post_id)


if __name__ == "__main__":
    seed()
