# Generated by Django 5.0.10 on 2025-02-10 10:31

from django.db import migrations
from django.db.backends.base.schema import BaseDatabaseSchemaEditor
from django.db.migrations.state import StateApps
from django.db.models import OuterRef


def set_default_for_can_summarize_topics_group(
    apps: StateApps, schema_editor: BaseDatabaseSchemaEditor
) -> None:
    Realm = apps.get_model("zerver", "Realm")
    NamedUserGroup = apps.get_model("zerver", "NamedUserGroup")

    Realm.objects.filter(can_summarize_topics_group=None).update(
        can_summarize_topics_group=NamedUserGroup.objects.filter(
            name="role:everyone", realm=OuterRef("id"), is_system_group=True
        ).values("pk")
    )


class Migration(migrations.Migration):
    atomic = False

    dependencies = [
        ("zerver", "0664_realm_can_summarize_topics_group"),
    ]

    operations = [
        migrations.RunPython(
            set_default_for_can_summarize_topics_group,
            elidable=True,
            reverse_code=migrations.RunPython.noop,
        )
    ]
