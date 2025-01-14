"""
Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
SPDX-License-Identifier: Apache-2.0
"""

SPARQL_OPTIONS = ['SELECT',
                  'INSERT'
                  'PREFIX',
                  'LIMIT',
                  'WHERE',
                  'OPTIONAL',
                  'CONSTRUCT',
                  'BIND',
                  'GRAPH',
                  'FILTER',
                  'ASK',
                  'DESCRIBE',
                  'UNLOAD']
GREMLIN_OPTIONS = [
    '.toString',
    '.tx',
    '.commit',
    '.rollback',
    '.withBulk',
    '.withPath',
    '.withSack',
    '.withSideEffect',
    '.addE',
    '.addV',
    '.inject',
    '.io',
    '.aggregate',
    '.and',
    '.as',
    '.barrier',
    '.both',
    '.bothE',
    '.bothV',
    '.branch',
    '.by',
    '.cap',
    '.choose',
    '.coalesce',
    '.coin',
    '.connectedComponent',
    '.constant',
    '.count',
    '.cyclicPath',
    '.dedup',
    '.drop',
    '.emit',
    '.filter',
    '.flatMap',
    '.fold',
    '.from',
    '.group',
    '.groupCount',
    '.has',
    '.hasId',
    '.hasKey',
    '.hasLabel',
    '.hasNot',
    '.hasValue',
    '.id',
    '.identity',
    '.in',
    '.inE',
    '.inV',
    '.index',
    '.is',
    '.iterate',
    '.key',
    '.label',
    '.limit',
    '.local',
    '.loops',
    '.map',
    '.match',
    '.math',
    '.max',
    '.mean',
    '.min',
    '.not',
    '.option',
    '.optional',
    '.or',
    '.order',
    '.otherV',
    '.out',
    '.outE',
    '.outV',
    '.pageRank',
    '.path',
    '.peerPressure',
    '.profile',
    '.project',
    '.properties',
    '.property',
    '.propertyMap',
    '.range',
    '.read',
    '.repeat',
    '.sack',
    '.sample',
    '.select',
    '.shortestPath',
    '.sideEffect',
    '.simplePath',
    '.skip',
    '.store',
    '.subgraph',
    '.sum',
    '.tail',
    '.timeLimit',
    '.times',
    '.to',
    '.toE',
    '.toV',
    '.tree',
    '.unfold',
    '.union',
    '.until',
    '.value',
    '.valueMap',
    '.values',
    '.where',
    '.with',
    '.write',
    '.Scope.local',
    '.global',
    '.Scope.global',
    '.T.id',
    '.T.label',
    '.T.key',
    '.T.value',
    '.incr',
    '.Order.incr',
    '.decr',
    '.Order.decr',
    '.asc',
    '.Order.asc',
    '.desc',
    '.Order.desc',
    '.shuffle',
    '.Order.shuffle',
    '.IN',
    '.OUT',
    '.BOTH',
    '.single',
    '.set',
    '.list',
    '.keys',
    '.first',
    '.last',
    '.all',
    '.mixed',
    '.addAll',
    '.assign',
    '.div',
    '.minus',
    '.mult',
    '.sumLong',
    '.any',
    '.none',
    '.negate',
    '.normSack',
    '.P.eq',
    '.eq',
    '.P.neq',
    '.neq',
    '.P.lt',
    '.lt',
    '.P.lte',
    '.lte',
    '.P.gt',
    '.gt',
    '.P.gte',
    '.gte',
    '.P.inside',
    '.inside',
    '.P.outside',
    '.outside',
    '.P.between',
    '.between',
    '.P.within',
    '.within',
    '.P.without',
    '.without',
    '.P.not',
    '.TextP.containing',
    '.containing',
    '.TextP.notContaining',
    '.notContaining',
    '.TextP.startingWith',
    '.startingWith',
    '.TextP.notStartingWith',
    '.notStartingWith',
    '.TextP.endingWith',
    '.endingWith',
    '.TextP.notEndingWith',
    '.notEndingWith',
    '.explain',
    '.hasNext',
    '.tryNext',
    '.next',
    '.toList',
    '.toSet',
    '.toBulkSet',
    '.edges',
    '.propertyName',
    '.target',
    '.distance',
    '.maxDistance',
    '.includeEdges',
    '.tokens',
    '.ids',
    '.labels',
    '.indexer',
    '.PageRank',
    '.PeerPressure',
    '.ShortestPath',
    '.WithOptions',
    '.datetime',
    '.null'
]
SPARQL_AND_GREMLIN = []
SPARQL_AND_GREMLIN.extend(SPARQL_OPTIONS)
SPARQL_AND_GREMLIN.extend(GREMLIN_OPTIONS)
for term in SPARQL_OPTIONS:
    SPARQL_AND_GREMLIN.append(term.lower())


# TODO: be able to determine if we should suggest SPARQL or Gremlin items
def get_completion_options(self, event):
    return SPARQL_AND_GREMLIN
