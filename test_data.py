from pydoc import describe

from django.contrib.auth.models import User

from links.models import Link, Vote

LINK_DATA = [
    {
        "title": "Irrational Exuberance",
        "url": "https://lethain.com/digg-v4/",
        "description": "Digg's v4 launch: an optimism born of necessity.",
    },
    {
        "title": "Messages that can only be understood under the influence of psychedelics (qri.org)",
        "url": "https://qri.org/blog/psycrypto-contest",
        "description": "Non-Ordinary States of Consciousness Contest: Psychedelic Cryptography (Innovate)",
    },
    {
        "title": "Passkeys now support external providers (developer.apple.com)",
        "url": "https://developer.apple.com/passkeys/",
        "description": "Passkeys can now be synced using external providers, and you can create groups to share passwords and passkeys. In managed environments, passkeys support Managed Apple IDs, including syncing via iCloud Keychain, and access controls let people easily restrict how passkeys are shared and synced.",
    },
]


def fill_links():
    submitter = User.objects.all()[0]
    for item in LINK_DATA:
        link = Link(title=item["title"], description=item["description"], url=item["url"], submitter=submitter)
        link.save()


def fill_votes():
    author = User.objects.all()[0]
    for i in range(100):
        Vote(link=Link.objects.order_by("?")[0], voter=author).save()


fill_links()
fill_votes()
