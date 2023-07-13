from django.utils.translation import gettext_lazy as _
from netbox.forms import NetBoxModelImportForm
from tenancy.models import *
from utilities.forms.fields import CSVModelChoiceField, SlugField

__all__ = (
    'ContactImportForm',
    'ContactGroupImportForm',
    'ContactRoleImportForm',
    'TenantImportForm',
    'TenantGroupImportForm',
)


#
# Tenants
#

class TenantGroupImportForm(NetBoxModelImportForm):
    parent = CSVModelChoiceField(
        label=_('Parent'),
        queryset=TenantGroup.objects.all(),
        required=False,
        to_field_name='name',
        help_text=_('Parent group')
    )
    slug = SlugField(
        label=_('Slug'),
    )

    class Meta:
        model = TenantGroup
        fields = ('name', 'slug', 'parent', 'description', 'tags')


class TenantImportForm(NetBoxModelImportForm):
    slug = SlugField(
        label=_('Slug'),
    )
    group = CSVModelChoiceField(
        label=_('Group'),
        queryset=TenantGroup.objects.all(),
        required=False,
        to_field_name='name',
        help_text=_('Assigned group')
    )

    class Meta:
        model = Tenant
        fields = ('name', 'slug', 'group', 'description', 'comments', 'tags')


#
# Contacts
#

class ContactGroupImportForm(NetBoxModelImportForm):
    parent = CSVModelChoiceField(
        label=_('Parent'),
        queryset=ContactGroup.objects.all(),
        required=False,
        to_field_name='name',
        help_text=_('Parent group')
    )
    slug = SlugField(
        label=_('Slug'),
    )

    class Meta:
        model = ContactGroup
        fields = ('name', 'slug', 'parent', 'description', 'tags')


class ContactRoleImportForm(NetBoxModelImportForm):
    slug = SlugField(
        label=_('Slug'),
    )

    class Meta:
        model = ContactRole
        fields = ('name', 'slug', 'description')


class ContactImportForm(NetBoxModelImportForm):
    group = CSVModelChoiceField(
        label=_('Group'),
        queryset=ContactGroup.objects.all(),
        required=False,
        to_field_name='name',
        help_text=_('Assigned group')
    )

    class Meta:
        model = Contact
        fields = ('name', 'title', 'phone', 'email', 'address', 'link', 'group', 'description', 'comments', 'tags')
