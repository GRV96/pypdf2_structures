from PyPDF2 import PdfFileReader

from arg_processing import\
	make_parser,\
	process_arguments,\
	StructureType
from pypdf2_structures import write_pdf_obj_struct


def _write_field_objs_in_stream(pdf_path, field_dict, w_stream, depth_limit):
	w_stream.write("Objects in the fields of " + str(pdf_path) + "\n")

	for mapping_name, field in field_dict.items():
		w_stream.write("\nField " + mapping_name + "\n")
		write_pdf_obj_struct(field, w_stream, depth_limit)


if __name__ == "__main__":
	try:
		struct_type = StructureType.FIELD
		parser = make_parser(struct_type)
		args = parser.parse_args()
		input_path, depth_limit, output_path\
			= process_arguments(args, struct_type)

	except ValueError as ve:
		print(ve)
		exit()

	reader = PdfFileReader(input_path.open(mode="rb"), strict=False)
	fields = reader.getFields()

	if output_path is None:
		from sys import stdout
		_write_field_objs_in_stream(input_path, fields, stdout, depth_limit)

	else:
		with output_path.open(mode="w", encoding="utf8") as output_stream:
			_write_field_objs_in_stream(
				input_path, fields, output_stream, depth_limit)
