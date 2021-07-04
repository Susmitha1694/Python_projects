from bookSchema import *
class CustomerRequestSchema(ModelSchema):
    class Meta(ModelSchema.Meta):
        model = CustomerRequest
        sqla_session = db.session
    id = fields.Number(dump_only=True)
    name = fields.String(required=True)
    phone = fields.String(required=True)
    address = fields.String(required=True)
    bookId = fields.Number(required=True)