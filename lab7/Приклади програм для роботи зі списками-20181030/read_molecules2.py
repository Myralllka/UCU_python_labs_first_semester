def read_all_molecules(reader):
    """ (file open for reading) -> list
    Read zero or more molecules from reader,
    returning a list of the molecules read.
    """
    result = []
    line = reader.readline()
    print(line)

    while line:
        molecule, line = read_molecule(reader, line)
        result.append(molecule)
    return result


def read_molecule(reader, line):
    """ (file open for reading, str) -> list
    Read a molecule from reader, where line refers to the first line of
    the molecule to be read. Return the molecule and the first line after
    it (or the empty string if the end of file has been reached).
    """
    fields = line.split()
    molecule = [fields[1]]
    line = reader.readline()
    while line and not line.startswith('COMPND'):
        fields = line.split()
        if fields[0] == 'ATOM':
            key, num, atom_type, x, y, z = fields
            molecule.append([atom_type, x, y, z])
            line = reader.readline()
    print("!!!!!!!!", molecule, line)
    return molecule, line

if __name__ == '__main__':
    molecule_file = open('multimol2.pdb', 'r')
    molecules = read_all_molecules(molecule_file)
    print(molecules)
