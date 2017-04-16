<h1><?= $row["title"] ?></h1>

<h4>
    Posted by <?= $row["username"] ?>
    on <?= date("Y-m-d", $row["created"]) ?>
    <?php
        if ($row["edited"] != 0) {
            echo "(last edited on " . date("Y-m-d", $row["edited"]) . ")";
        }
    ?>
</h4>

<div class="post-body">
    <?= $row["body"] ?>
</div>
