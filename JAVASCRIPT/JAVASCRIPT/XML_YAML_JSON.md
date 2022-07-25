# XML
```xml
<!-- everything including the tags is a single element -->
<!-- xml prolog -->
<?xml version="1.0" encoding="UTF-8"?>
<!-- mandatory root, nesting -->
<root>
  <child>
    <subchild>
      <p>
        <i>
          <!-- mandatory closures -->
          This is properly nested paragraph in italics.
        </i>
      </p>
      <p>
        <!-- attribute values are quoted and for metadata-->
        <note date="1970-01-01">
        <!-- elements are for explicit content -->
          <date>
            <year>1970</year>
            <month>01</month>
            <day>01</day>
          </date>
        </note>
      </p>
      <!-- illegal characters are
      &lt;	<	less than
      &gt;	>	greater than
      &amp;	&	ampersand
      &apos;	'	apostrophe
      &quot;	"	quotation mark  -->
      <br />
    </subchild>
  </child>
</root>
```
# YAML
```yaml
- something
    indentation: more
    indentation2: yet more
- something-else
    special-spec: 9000
    yet-another-spec: 0
      for-real: 1
      really: 1
```
# JSON
```json
const obj1 = {
    "string":"John",
    "number":30,
    "obj2:{"string2":"Smith"},
    "array":["brackets1", "brackets2"],
    "boolean":False,
    "empty":null
}
```
