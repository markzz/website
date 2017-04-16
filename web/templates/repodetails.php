<h1>Arch Linux Repository - <?= $repo ?></h1>

<h3><?= $row["desc"] ?></h3>

<h3>Package List</h3>

<table>
    <tr>
        <th>Name</th>
        <th>Version</th>
        <th>Description</th>
        <th>Architecture</th>
        <th>Date Packaged</th>
        <th>Download</th>
        <?php if ($row["signed"]): ?><th>Signature</th><?php endif; ?>
    </tr>

    <?php foreach ($pkglist as $pkg): ?>
        <tr>
            <?php $url = $row["url"] . "/" . $pkg->name . "-" . $pkg->version . "-" . $pkg->arch . ".pkg.tar.xz"; ?>
            <td><?= $pkg->name ?></td>
            <td><?= $pkg->version ?></td>
            <td><?= $pkg->desc ?></td>
            <td><?= $pkg->arch ?></td>
            <td><?= date("Y-m-d H:i", $pkg->builddate) ?></td>
            <td><a href="<?= $url ?>">Download</a></td>
            <?php if ($row["signed"]): ?><td><a href="<?= $url ?>.sig">Sig</a></td><?php endif; ?>
        </tr>
    <?php endforeach; ?>

</table>