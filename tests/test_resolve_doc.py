import asddoc
import os


class TestResolveDoc:
    def test_name(self, tmpdir):
        asddoc.cfg.BASEDIR = tmpdir

        res = asddoc.resolve_doc('name')
        assert res == f'{tmpdir}/name.md'

    def test_folder(self, tmpdir):
        asddoc.cfg.BASEDIR = tmpdir
        os.mkdir(f'{tmpdir}/folder')

        res = asddoc.resolve_doc('folder')
        assert res == f'{tmpdir}/folder/folder.md'

    def test_folder_symlink(self, tmpdir):
        asddoc.cfg.BASEDIR = tmpdir
        os.mkdir(f'{tmpdir}/folder')
        os.symlink(f'{tmpdir}/folder', f'{tmpdir}/some')

        res = asddoc.resolve_doc('some')
        assert res == f'{tmpdir}/folder/folder.md'

    def test_symfolder_file(self, tmpdir):
        # <sym>/file.md
        asddoc.cfg.BASEDIR = tmpdir
        os.mkdir(f'{tmpdir}/folder')
        open(f'{tmpdir}/folder/file.md', 'w').close()
        os.symlink(f'{tmpdir}/folder', f'{tmpdir}/some')

        res = asddoc.resolve_doc('some/file')
        assert res == f'{tmpdir}/folder/file.md'

    def test_folder_symfolder_symfile(self, tmpdir):
        # <sym>/file.md
        asddoc.cfg.BASEDIR = tmpdir
        os.mkdir(f'{tmpdir}/folder')
        open(f'{tmpdir}/folder/file.md', 'w').close()
        os.symlink(f'{tmpdir}/folder', f'{tmpdir}/some')

        res = asddoc.resolve_doc('some/file')
        assert res == f'{tmpdir}/folder/file.md'
