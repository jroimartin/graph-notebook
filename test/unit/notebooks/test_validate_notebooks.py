"""
Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
SPDX-License-Identifier: Apache-2.0
"""

import json
import unittest

from graph_notebook.notebooks.install import get_all_notebooks_paths, NOTEBOOK_BASE_DIR


class TestValidateAllNotebooks(unittest.TestCase):
    maxDiff = None

    def test_no_extra_notebooks(self):
        """
        hard-coded the expected paths for notebooks so that adding new ones is intentional.
        """

        expected_paths = [
            f'{NOTEBOOK_BASE_DIR}/01-Getting-Started/01-About-the-Neptune-Notebook.ipynb',
            f'{NOTEBOOK_BASE_DIR}/01-Getting-Started/02-Using-Gremlin-to-Access-the-Graph.ipynb',
            f'{NOTEBOOK_BASE_DIR}/01-Getting-Started/03-Using-RDF-and-SPARQL-to-Access-the-Graph.ipynb',
            f'{NOTEBOOK_BASE_DIR}/01-Getting-Started/04-Social-Network-Recommendations-with-Gremlin.ipynb',
            f'{NOTEBOOK_BASE_DIR}/02-Visualization/Air-Routes-Gremlin.ipynb',
            f'{NOTEBOOK_BASE_DIR}/02-Visualization/Air-Routes-SPARQL.ipynb',
            f'{NOTEBOOK_BASE_DIR}/02-Visualization/Blog Workbench Visualization.ipynb',
            f'{NOTEBOOK_BASE_DIR}/02-Visualization/EPL-Gremlin.ipynb',
            f'{NOTEBOOK_BASE_DIR}/02-Visualization/EPL-SPARQL.ipynb',
            f'{NOTEBOOK_BASE_DIR}/02-Visualization/Visualization-Grouping-Coloring-Gremlin.ipynb',
            f'{NOTEBOOK_BASE_DIR}/03-Sample-Applications/00-Sample-Applications-Overview.ipynb',
            f'{NOTEBOOK_BASE_DIR}/03-Sample-Applications/01-Fraud-Graphs/01-Building-a-Fraud-Graph-Application.ipynb',
            f'{NOTEBOOK_BASE_DIR}/03-Sample-Applications/02-Knowledge-Graphs/01-Building-a-Knowledge-Graph-Application.ipynb',
            f'{NOTEBOOK_BASE_DIR}/03-Sample-Applications/03-Identity-Graphs/01-Building-an-Identity-Graph-Application.ipynb',
            f'{NOTEBOOK_BASE_DIR}/04-Machine-Learning/Neptune-ML-00-Getting-Started-with-Neptune-ML-Gremlin.ipynb',
            f'{NOTEBOOK_BASE_DIR}/04-Machine-Learning/Neptune-ML-01-Introduction-to-Node-Classification-Gremlin.ipynb',
            f'{NOTEBOOK_BASE_DIR}/04-Machine-Learning/Neptune-ML-02-Introduction-to-Node-Regression-Gremlin.ipynb',
            f'{NOTEBOOK_BASE_DIR}/04-Machine-Learning/Neptune-ML-03-Introduction-to-Link-Prediction-Gremlin.ipynb']
        notebook_paths = get_all_notebooks_paths()
        expected_paths.sort()
        notebook_paths.sort()

        self.assertEqual(len(expected_paths), len(notebook_paths))
        for i in range(len(expected_paths)):
            self.assertEqual(expected_paths[i], notebook_paths[i])

    def test_validate_notebooks_have_no_output(self):
        notebooks = get_all_notebooks_paths()
        for n in notebooks:
            with open(n, 'r') as notebook_file:
                file_content = notebook_file.read()
                nb_content = json.loads(file_content)
                for cell in nb_content['cells']:
                    if 'cell_type' in cell and cell['cell_type'] == 'code':
                        self.assertEqual(0, len(cell['outputs']))

    def test_readme_and_overview_match(self):
        notebook_file_path = f'{NOTEBOOK_BASE_DIR}/03-Sample-Applications/00-Sample-Applications-Overview.ipynb'
        readme_file_path = f'{NOTEBOOK_BASE_DIR}/03-Sample-Applications/README.md'

        with open(notebook_file_path, 'r') as notebook_file:
            notebook_js = json.load(notebook_file)

        with open(readme_file_path, 'r') as readme_file:
            readme_content = readme_file.read()

        notebook_content = ''
        notebook_content = notebook_content.join(notebook_js['cells'][0]['source'])

        self.assertEqual(notebook_js['cells'][0]['cell_type'], 'markdown')
        self.assertEqual(readme_content, notebook_content)
