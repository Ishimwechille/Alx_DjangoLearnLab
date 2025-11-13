# Django Permissions and Groups Setup

## Custom Permissions
Defined in `Article` model:
- `can_view` → Allows viewing articles
- `can_create` → Allows creating new articles
- `can_edit` → Allows editing articles
- `can_delete` → Allows deleting articles

## Groups
Configured automatically in `apps.py`:
- **Viewers**: `can_view`
- **Editors**: `can_view`, `can_create`, `can_edit`
- **Admins**: All permissions

## Usage
In views:
- Use decorators like `@permission_required('relationship_app.can_edit')` to protect routes.
- Users without the required permission receive a 403 response.
