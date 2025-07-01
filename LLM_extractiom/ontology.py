
import rdflib

# Load the OWL file
ontology_path = 'MALOnt/MALOnt.owl'  # Path to your OWL file
g = rdflib.Graph()
g.parse(ontology_path)

# Define namespaces
namespace_owl = rdflib.URIRef("http://www.w3.org/2002/07/owl#")
namespace_rdfs = rdflib.URIRef("http://www.w3.org/2000/01/rdf-schema#")
namespace_malont = rdflib.URIRef("http://idea.rpi.edu/malont#")

# 1. Extract Classes (Entities) from the ontology
classes = set()
for s, p, o in g.triples((None, rdflib.RDF.type, rdflib.OWL.Class)):
    classes.add(s)

print("Classes (Entities):")
for cls in classes:
    print(cls)

# 2. Extract Object Properties (Relationships) from the ontology
object_properties = set()
for s, p, o in g.triples((None, rdflib.RDF.type, rdflib.OWL.ObjectProperty)):
    object_properties.add(s)

print("\nObject Properties (Relationships):")
for obj_prop in object_properties:
    print(obj_prop)