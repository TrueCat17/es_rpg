""" Encoding Aliases Support

    This module is used by the encodings package search function to
    map encodings names to module names.

    Note that the search function normalizes the encoding names before
    doing the lookup, so the mapping will have to map normalized
    encoding names to module names.

    Contents:

        The following aliases dictionary contains mappings of all IANA
        character set names for which the Python core library provides
        codecs. In addition to these, a few Python specific codec
        aliases have also been added.

"""
aliases = {

    # Please keep this list sorted alphabetically by value !

    # ascii codec
    '646'                : 'ascii',
    'ansi_x3.4_1968'     : 'ascii',
    'ansi_x3_4_1968'     : 'ascii', # some email headers use this non-standard name
    'ansi_x3.4_1986'     : 'ascii',
    'cp367'              : 'ascii',
    'csascii'            : 'ascii',
    'ibm367'             : 'ascii',
    'iso646_us'          : 'ascii',
    'iso_646.irv_1991'   : 'ascii',
    'iso_ir_6'           : 'ascii',
    'us'                 : 'ascii',
    'us_ascii'           : 'ascii',

    # base64_codec codec
    'base64'             : 'base64_codec',
    'base_64'            : 'base64_codec',

    # hex_codec codec
    'hex'                : 'hex_codec',

    # latin_1 codec
    #
    # Note that the latin_1 codec is implemented internally in C and a
    # lot faster than the charmap codec iso8859_1 which uses the same
    # encoding. This is why we discourage the use of the iso8859_1
    # codec and alias it to latin_1 instead.
    #
    '8859'               : 'latin_1',
    'cp819'              : 'latin_1',
    'csisolatin1'        : 'latin_1',
    'ibm819'             : 'latin_1',
    'iso8859'            : 'latin_1',
    'iso8859_1'          : 'latin_1',
    'iso_8859_1'         : 'latin_1',
    'iso_8859_1_1987'    : 'latin_1',
    'iso_ir_100'         : 'latin_1',
    'l1'                 : 'latin_1',
    'latin'              : 'latin_1',
    'latin1'             : 'latin_1',

    # mbcs codec
    'dbcs'               : 'mbcs',

    # utf_16 codec
    'u16'                : 'utf_16',
    'utf16'              : 'utf_16',

    # utf_16_be codec
    'unicodebigunmarked' : 'utf_16_be',
    'utf_16be'           : 'utf_16_be',

    # utf_16_le codec
    'unicodelittleunmarked' : 'utf_16_le',
    'utf_16le'           : 'utf_16_le',

    # utf_32 codec
    'u32'                : 'utf_32',
    'utf32'              : 'utf_32',

    # utf_32_be codec
    'utf_32be'           : 'utf_32_be',

    # utf_32_le codec
    'utf_32le'           : 'utf_32_le',

    # utf_8 codec
    'u8'                 : 'utf_8',
    'utf'                : 'utf_8',
    'utf8'               : 'utf_8',
    'utf8_ucs2'          : 'utf_8',
    'utf8_ucs4'          : 'utf_8',
    
    # zlib_codec codec
    'zip'                : 'zlib_codec',
    'zlib'               : 'zlib_codec',
}
