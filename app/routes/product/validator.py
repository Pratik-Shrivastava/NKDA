from marshmallow import Schema, fields, validate


class AddProductValidator(Schema):
    product_name = fields.String(required=True)
    product_description = fields.String()
    product_price = fields.Float(required=True)
    created_by = fields.String(required=True)
    updated_at = fields.DateTime()


class UpdateProductValidator(Schema):
    product_id = fields.Integer(required=True, validate=validate.Range(min=1))
    product_name = fields.String(required=True)
    product_description = fields.String()
    product_price = fields.Float(required=True)
    updated_at = fields.DateTime()


class GetProductValidator(Schema):
    product_id = fields.Integer(required=True, validate=validate.Range(min=1))


class DeleteProductValidator(Schema):
    product_id = fields.Integer(required=True, validate=validate.Range(min=1))
