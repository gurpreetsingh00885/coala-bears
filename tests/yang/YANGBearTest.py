from bears.yang.YANGBear import YANGBear
from coalib.testing.LocalBearTestHelper import verify_local_bear


COALA_MODEL = """
module coala-model {

  namespace "http://coala.io/yang/coala-model";
  prefix coala;

  organization coala.io;
  contact "yang@coala.io";
  description "The coala code analysis YANG model";

  revision 2017-08-02 {
    description "Test version";
    reference "http://coala.io/yang";
  }

  list bears {
    key name;
    description "All available coala Bears";

    leaf name {
      type string;
      description "The name of the coala Bear";
    }
  }
}
"""


# several missing module sub-statements
MISSING_STATEMENTS = """
module invalid-model {

  namespace "http://coala.io/yang/invalid-model";
  prefix invalid;
}
"""


YANGBearTest = verify_local_bear(
    YANGBear, valid_files=(COALA_MODEL, ),
    invalid_files=(MISSING_STATEMENTS, ))
